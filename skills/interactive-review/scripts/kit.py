"""Decision components for an interactive review page, in the broadsheet-audit design.

Import from a page builder:

    import sys; sys.path.insert(0, "<skill>/scripts")
    from kit import CSS, action_bar, decision_block, script

Put CSS after the design's own stylesheet, action_bar() under the "how to
answer" note, decision_block(id) under each item's key-value table, and
script(ids) before </body>. Markup and CSS follow the Decision block, Choice
control, Notes field, Action bar, Buttons, Status line and Reply thread
sections of designs/broadsheet-audit/design.md.
"""

from __future__ import annotations

import html
import json

ITEM_OPTIONS = [("apply", "Apply"), ("skip", "Skip"), ("discuss", "Discuss")]

CSS = """
.dec { border:1px solid #000; padding:.4rem .6rem; margin:0 0 1rem; }
.opt { display:inline-block; margin-right:1.2rem; font-size:14px; cursor:pointer; }
.dec textarea { display:block; width:100%; margin-top:.4rem; border:1px solid #000; border-radius:0;
  padding:.3rem .4rem; font:13px/1.4 Georgia,"Times New Roman",serif; background:#fff; }
.dec textarea:focus, button:focus-visible { outline:2px solid #000; outline-offset:0; }
.actions { border:2px solid #000; padding:.5rem .7rem; margin:1rem 0; display:flex; gap:1rem; flex-wrap:wrap; align-items:center; }
button { font:14px Georgia,"Times New Roman",serif; background:#000; color:#fff; border:1px solid #000;
  border-radius:0; padding:.35rem .9rem; cursor:pointer; }
button.secondary { background:#fff; color:#000; }
button:hover { text-decoration:underline; }
.status { font-size:12.8px; color:#333; }
.replies { border-top:1px solid #000; margin-top:.5rem; padding-top:.3rem; font-size:12.5px; }
.replies:empty { display:none; }
.reply .at { font-size:11.3px; color:#333; margin-right:.4rem; }
"""


def decision_block(item_id: str, options: list[tuple[str, str]] | None = None) -> str:
    """Choice row, notes field and an empty reply thread for one item."""
    choices = "".join(
        f'<label class="opt"><input type="radio" name="{item_id}" value="{value}"> {html.escape(label)}</label>'
        for value, label in (options or ITEM_OPTIONS)
    )
    return (
        f'<div class="dec" data-id="{item_id}">{choices}'
        f'<textarea name="{item_id}-note" rows="2" placeholder="Notes for this item"></textarea>'
        f'<div class="replies" id="r-{item_id}"></div></div>'
    )


def action_bar() -> str:
    """Send, copy and the status line, plus the page-wide reply thread under them."""
    return (
        '<div class="actions"><button id="send">Send decisions</button>'
        '<button class="secondary" id="copy">Copy as text</button>'
        '<span class="status" id="status">Not sent yet.</span></div>'
        '<div class="replies" id="r-_global"></div>'
    )


def script(item_ids: list[str]) -> str:
    """Restore saved answers, poll replies every 4 s, send to /decisions, copy as text."""
    return """<script>
const IDS = %s;
let dirty = false;
const served = location.protocol.startsWith('http');
const status = (t) => { document.getElementById('status').textContent = t; };
function collect() {
  const out = {};
  for (const id of IDS) {
    const c = document.querySelector(`input[name="${id}"]:checked`);
    const n = document.querySelector(`textarea[name="${id}-note"]`).value.trim();
    if (c || n) out[id] = { choice: c ? c.value : null, note: n };
  }
  return out;
}
function restore(decisions) {
  for (const [id, d] of Object.entries(decisions || {})) {
    if (d.choice) { const el = document.querySelector(`input[name="${id}"][value="${d.choice}"]`); if (el) el.checked = true; }
    const ta = document.querySelector(`textarea[name="${id}-note"]`); if (ta && d.note) ta.value = d.note;
  }
}
function renderReplies(replies) {
  for (const [id, list] of Object.entries(replies || {})) {
    const box = document.getElementById('r-' + id); if (!box) continue;
    box.innerHTML = '';
    for (const r of list) {
      const p = document.createElement('div'); p.className = 'reply';
      const at = document.createElement('span'); at.className = 'at'; at.textContent = 'Reply ' + r.at;
      p.appendChild(at); p.appendChild(document.createTextNode(r.text)); box.appendChild(p);
    }
  }
}
async function poll(first) {
  if (!served) return;
  try {
    const s = await (await fetch('/state', { cache: 'no-store' })).json();
    if (first) restore(s.decisions);
    renderReplies(s.replies);
    if (!dirty && s.saved_at) status('Sent ' + s.saved_at + '.');
  } catch (e) { status('Server not reachable. Use Copy as text.'); }
}
document.addEventListener('input', () => { dirty = true; status('Unsent changes.'); });
document.getElementById('send').onclick = async () => {
  if (!served) { status('Opened as a file. Open the served address to send, or use Copy as text.'); return; }
  const r = await fetch('/decisions', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ decisions: collect() }) });
  if (r.ok) { dirty = false; status('Sent ' + (await r.json()).saved_at + '.'); } else status('Send failed: ' + r.status + '.');
};
document.getElementById('copy').onclick = async () => {
  const lines = Object.entries(collect()).map(([id, d]) => `${id}: ${d.choice || '-'}${d.note ? ' | ' + d.note : ''}`);
  await navigator.clipboard.writeText(lines.join('\\n'));
  status('Copied ' + lines.length + ' answers.');
};
if (!served) status('Opened as a file. Open the served address to send.');
poll(true);
setInterval(() => poll(false), 4000);
</script>""" % json.dumps(item_ids)
