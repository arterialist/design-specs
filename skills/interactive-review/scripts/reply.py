"""Append a reply under an item on an interactive review page.

Usage: reply.py <state.json> <item_id or _global> <text>

The page polls the state file through review_server.py and shows replies under
the matching decision block within a few seconds. Decisions are left untouched.
"""

import json
import sys
import time
from pathlib import Path

state_path, item_id, text = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
try:
    state = json.loads(state_path.read_text())
except (FileNotFoundError, json.JSONDecodeError):
    state = {"decisions": {}, "replies": {}, "saved_at": None, "history": []}
state.setdefault("replies", {}).setdefault(item_id, []).append(
    {"at": time.strftime("%H:%M"), "text": text}
)
state_path.write_text(json.dumps(state, indent=1, ensure_ascii=False))
print("replied", item_id)
