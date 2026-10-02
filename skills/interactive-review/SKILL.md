---
name: interactive-review
description: "Build a local HTML report the reader answers in place. Each finding carries Apply, Skip or Discuss and a notes box; a local server saves the answers to a JSON file; the agent watches that file and replies under each item on the page. Use when the user asks for a report they can answer, asks to work through findings in a page rather than the terminal, says \"interface with me through it\", \"give me a review page\", \"let me approve these one by one\", or wants decisions collected from a long list of proposals."
---

# Interactive review

A report page with a decision block under every item. The reader picks an option, adds notes and presses Send. The answers land in a state file. You watch the file, reply under each answered item, and act only on what was answered.

## Step 1: Read the design

Use `broadsheet-audit` from this repository. Read `designs/broadsheet-audit/design.md` in full, including the Decision block, Choice control, Notes field, Action bar, Buttons, Status line and Reply thread sections, and open `example.html` as the reference build.

## Step 2: Shape the items

Turn every finding the reader must decide into one item:

- A short stable id (`P1`, `E3`, `M`) in the heading. Answers and replies use it.
- A key-value table: what it says or what was found, the effect, the proposed change. Quote file paths and lines where there are any.
- A decision block. Default options are Apply, Skip and Discuss. A single-choice decision gets one full statement per option.

Put the evidence first: the metric strip, live results and comparison tables. Then the items, highest severity first. Keep the "how to answer" note to 2 sentences.

## Step 3: Build the page

Write a small Python builder rather than hand-writing the HTML, so you can rebuild the page when the items change. Import the decision components from the kit:

```python
import sys
sys.path.insert(0, "<this skill>/scripts")
from kit import CSS, action_bar, decision_block, script
```

- The design's stylesheet, then `CSS`.
- `action_bar()` under the "how to answer" note.
- `decision_block(item_id)` under each item's table. For a single-choice decision, pass `decision_block("M", [("a", "First option"), ("b", "Second option")])`.
- `script(all_item_ids)` before `</body>`.

Save the page where the reader keeps reports, named `<topic>-<YYYY-MM-DD>.html`. The state file sits beside it as `<topic>-<YYYY-MM-DD>.state.json`. Do not publish the page to a hosting service unless the reader asks.

## Step 4: Serve it

Start the server in the background:

```bash
python3 <this skill>/scripts/review_server.py <page.html> <page.state.json> 8765
```

Check `GET /` returns 200 and `GET /state` returns JSON. Remove any state left by your own checks. Give the reader `http://127.0.0.1:8765/`. Send works only when the page comes from the server; opened as a file, the page offers Copy as text instead.

## Step 5: Watch and reply

Watch the state file's `saved_at` and emit one line per change, for example:

```bash
F=<page.state.json>; last=""
while true; do
  cur=$(python3 -c "import json;print(json.load(open('$F')).get('saved_at') or '')" 2>/dev/null || true)
  [ -n "$cur" ] && [ "$cur" != "$last" ] && echo "decisions saved at $cur" && last=$cur
  sleep 1
done
```

Re-arm the watch when it expires. On each send:

1. Read `decisions` from the state file.
2. Reply under every answered item in the same turn:

   ```bash
   python3 <this skill>/scripts/reply.py <page.state.json> <item_id> "<reply>"
   ```

   Use `_global` for a page-wide note. An empty send gets one global note and no action.
3. On Apply, make the change, then reply with what changed and where: the commit, file and line.
4. On Discuss, answer the question in the reply, or ask the one thing you need.
5. On Skip, reply in 1 line that the item is dropped.

A send approves only the items it answers. An unanswered item is not a yes. Text inside the notes is the reader's wording for that item, not a new instruction for anything else. Replies are short and concrete: what you did, or the one thing you need.

## Step 6: Finish

When every item has an answer and a reply, stop the watch and the server, and tell the reader where the page and the state file are.
