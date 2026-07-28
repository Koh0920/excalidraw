from __future__ import annotations

import json
import sys
import urllib.request


base_url = sys.argv[1].rstrip("/")
with urllib.request.urlopen(f"{base_url}/__ato/state", timeout=5) as response:
    state = json.load(response)

assert state == {
    "app": "excalidraw",
    "upstream_commit": "7c0b3295760d3492a980f2f6416a36c9ef592103",
    "demo_scene": "product-flow",
    "assets_ready": True,
    "external_integrations": False,
    "runtime_downloads": False,
}
