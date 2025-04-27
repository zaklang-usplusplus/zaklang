#!/usr/bin/env python3
import sys
import json
from pathlib import Path

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def main():
    if len(sys.argv) < 2:
        print("Usage: router.py <fractal-file>")
        sys.exit(1)

    fractal_path = Path(sys.argv[1])
    if not fractal_path.exists():
        print(f"Fractal file not found: {fractal_path}")
        sys.exit(1)

    # Load fractal
    fractal = load_json(fractal_path)

    # Load council.json from project root
    council_path = Path(__file__).resolve().parent.parent / "council.json"
    if not council_path.exists():
        print("council.json not found")
        sys.exit(1)

    council = load_json(council_path)

    print("🧠 Fractal and council loaded. Ready to match.")

if __name__ == "__main__":
    main()

