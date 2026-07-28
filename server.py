from __future__ import annotations

import http.server
import json
import os
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent
BUILD = ROOT / "excalidraw-app" / "build"
UPSTREAM_COMMIT = "7c0b3295760d3492a980f2f6416a36c9ef592103"


class CapsuleHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BUILD), **kwargs)

    def do_GET(self) -> None:
        path = urlsplit(self.path).path
        if path == "/health":
            self._json({"status": "ok"})
            return
        if path == "/__ato/state":
            self._json(
                {
                    "app": "excalidraw",
                    "upstream_commit": UPSTREAM_COMMIT,
                    "demo_scene": "product-flow",
                    "assets_ready": (BUILD / "index.html").is_file()
                    and (BUILD / "assets").is_dir(),
                    "external_integrations": False,
                    "runtime_downloads": False,
                }
            )
            return
        if path == "/":
            self.send_response(302)
            self.send_header("Location", "/?ato-demo=1")
            self.end_headers()
            return
        requested = (BUILD / path.lstrip("/")).resolve()
        if not requested.is_relative_to(BUILD) or not requested.is_file():
            self.path = "/index.html"
        super().do_GET()

    def end_headers(self) -> None:
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data: blob:; font-src 'self' data:; connect-src 'self'; "
            "worker-src 'self' blob:; media-src 'self' blob:; object-src 'none'; "
            "base-uri 'self'; frame-ancestors *",
        )
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()

    def _json(self, payload: dict[str, object]) -> None:
        body = json.dumps(payload, separators=(",", ":")).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)


port = int(os.environ.get("ATO_PORT", "8080"))
http.server.ThreadingHTTPServer(("0.0.0.0", port), CapsuleHandler).serve_forever()
