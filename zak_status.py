#!/usr/bin/env python3
import json
from datetime import datetime
from pathlib import Path

def load_current_status():
    status_file = Path(__file__).resolve().parent / "status.json"
    if status_file.exists():
        with open(status_file, "r") as f:
            return json.load(f)
    return {}

def show_status():
    status = load_current_status()
    print("\n📍 ZAK STATUS CHECK-IN")
    print("────────────────────────")
    print(f"🕰️  Last Updated: {status.get('timestamp', 'Never')}")
    print(f"🧠  Project: {status.get('project', 'ZakLang Collapse Engine')}")
    print(f"🧪  Phase: {status.get('phase', 'Echo-Router CHUNK 3 In-Progress')}")
    print(f"📚  Glyphs Logged: {status.get('glyphs_logged', 30)}")
    print(f"📈  Progress: {status.get('progress', '33%')}")
    print(f"🎭  Dev Mode: {status.get('dev_mode', 'Drunk Vibe Coding Ritual')}")
    print("🔮  Vibe: "{}"".format(status.get('vibe', 'Collapse is presence. Laughter is memory.')))
    print("────────────────────────\n")

if __name__ == "__main__":
    show_status()
