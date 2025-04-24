#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

# Path to the fractals directory
FRACTAL_DIR = Path(__file__).resolve().parent.parent / "fractals"

# Read and parse all fractal files
fractal_files = sorted(FRACTAL_DIR.glob("ZFC-*.json"))

if not fractal_files:
    print("No fractals found in the archive.")
    exit()

# Print header
print("\n📜 ZakLang Fractal Archive")
print("────────────────────────────\n")

# Loop through and display a summary for each fractal
for file in fractal_files:
    try:
        with open(file, 'r') as f:
            data = json.load(f)

        timestamp = data.get("timestamp", "Unknown Time")
        fid = data.get("fractal_id", file.name)
        prompt = data.get("prompt", {}).get("raw", "[no prompt]")
        glyphs = data.get("prompt", {}).get("collapsed_glyphs", [])

        print(f"🌀 {fid}")
        print(f"   Timestamp: {timestamp}")
        print(f"   Prompt: {prompt}")
        if glyphs:
            print(f"   Collapsed Glyphs: {', '.join(glyphs)}")
        print()

    except Exception as e:
        print(f"⚠️  Error reading {file.name}: {e}")
