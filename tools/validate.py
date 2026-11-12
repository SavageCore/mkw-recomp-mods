"""mod.json checks, same as the release workflow: run `make validate`."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ok = True
for meta in sorted((ROOT).glob("*/mod.json")):
    try:
        m = json.loads(meta.read_text())
    except ValueError as e:
        print(f"{meta.name}: invalid JSON: {e}")
        ok = False
        continue
    for k in ("name", "title", "has_romfs", "switches"):
        if k not in m:
            print(f"{meta.name}: misses {k!r}")
            ok = False
    for p in m.get("patches", {}).get("spans", []) + m.get("patches", {}).get("sites", []):
        for k in ("set", "env", "module", "off"):
            if k not in p:
                print(f"{meta.name}: patch misses {k!r}")
                ok = False
        if not str(p.get("env", "")).startswith("MKW_"):
            print(f"{meta.name}: env switch needs its MKW_ prefix")
            ok = False
sys.exit(0 if ok else 1)
