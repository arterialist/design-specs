"""Serve an interactive review page and keep the reader's answers.

Usage: review_server.py <page.html> <page.state.json> [port, default 8765]

GET  /         the report
GET  /state    {"decisions": {...}, "replies": {...}, "saved_at": ...}
POST /decisions  body {"decisions": {...}}; written to the state file
The agent writes replies into the same state file; the page never does.
"""

from __future__ import annotations

import json
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PAGE = Path(sys.argv[1])
STATE = Path(sys.argv[2])
PORT = int(sys.argv[3]) if len(sys.argv) > 3 else 8765


def read_state() -> dict:
    try:
        return json.loads(STATE.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {"decisions": {}, "replies": {}, "saved_at": None, "history": []}


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, body: bytes, kind: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", kind)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        if self.path.split("?")[0] in ("/", "/index.html"):
            self._send(200, PAGE.read_bytes(), "text/html; charset=utf-8")
        elif self.path.startswith("/state"):
            self._send(200, json.dumps(read_state()).encode(), "application/json")
        else:
            self._send(404, b"not found", "text/plain")

    def do_POST(self) -> None:  # noqa: N802
        if not self.path.startswith("/decisions"):
            self._send(404, b"not found", "text/plain")
            return
        raw = self.rfile.read(int(self.headers.get("Content-Length") or 0))
        try:
            decisions = json.loads(raw)["decisions"]
        except (ValueError, KeyError):
            self._send(400, b"bad body", "text/plain")
            return
        state = read_state()
        state["decisions"] = decisions
        state["saved_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
        state.setdefault("history", []).append({"at": state["saved_at"], "decisions": decisions})
        STATE.write_text(json.dumps(state, indent=1, ensure_ascii=False))
        self._send(200, json.dumps({"saved_at": state["saved_at"]}).encode(), "application/json")

    def log_message(self, *args: object) -> None:
        return


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
