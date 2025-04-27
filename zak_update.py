#!/usr/bin/env python3
import argparse
import json
from datetime import datetime
from pathlib import Path

status_file = Path(__file__).resolve().parent / "status.json"
log_file = Path(__file__).resolve().parent / "status_log.jsonl"

def load_status():
    if status_file.exists():
        with open(status_file, "r") as f:
            return json.load(f)
    return {}

def save_status(data):
    with open(status_file, "w") as f:
        json.dump(data, f, indent=2)

def append_log(data):
    with open(log_file, "a") as f:
        f.write(json.dumps(data) + "\n")

def update_status(args):
    now = datetime.utcnow().isoformat() + "+00:00"
    current = load_status()
    updated = {
        "timestamp": now,
        "project": current.get("project", "ZakLang Collapse Engine"),
        "phase": args.phase or current.get("phase", "Unspecified Phase"),
        "glyphs_logged": args.glyphs if args.glyphs is not None else current.get("glyphs_logged", 0),
        "progress": f"{args.progress}%" if args.progress is not None else current.get("progress", "0%"),
        "dev_mode": current.get("dev_mode", "Drunk Vibe Coding Ritual"),
        "vibe": args.vibe or current.get("vibe", "Unspecified")
    }
    save_status(updated)
    append_log(updated)
    print("\n✅ Status updated and logged:")
    print(json.dumps(updated, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update ZakLang Project Status")
    parser.add_argument("--phase", type=str, help="Current dev phase description")
    parser.add_argument("--glyphs", type=int, help="Total glyphs logged")
    parser.add_argument("--progress", type=int, help="Estimated project completion percentage")
    parser.add_argument("--vibe", type=str, help="One-line vibe descriptor")

    args = parser.parse_args()
    update_status(args)
