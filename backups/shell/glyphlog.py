#!/usr/bin/env python3
import json
import os
from datetime import datetime, timezone
from pathlib import Path

# Set up the directory
FRACTAL_DIR = Path(__file__).resolve().parent.parent / "fractals"
FRACTAL_DIR.mkdir(parents=True, exist_ok=True)

# Prompt user for input
prompt = input("Enter your prompt (glyph seed): ")

# Generate timestamp
timestamp = datetime.now(timezone.utc).isoformat(timespec='seconds')
fractal_id = f"ZFC-{timestamp.replace(':', '-')}"
filename = FRACTAL_DIR / f"{fractal_id}.json"

# Define basic memory fractal structure
fractal = {
    "fractal_id": fractal_id,
    "timestamp": timestamp,
    "prompt": {
        "raw": prompt,
        "collapsed_glyphs": []
    },
    "context": {
        "shell_state": "python-init",
        "collapse_depth": 1,
        "prior_glyphs": []
    },
    "router_trace": {
        "invoked_models": [],
        "routing_logic": "manual input"
    },
    "dialectic_log": [],
    "collapse_vector": {
        "selected_output": None,
        "justification": None
    },
    "feedback": {
        "user_confirmation": None,
        "resonance_score": None
    },
    "echoes": {
        "seeded_glyphs": [],
        "future_integration": []
    }
}

# Save to file
with open(filename, 'w') as f:
    json.dump(fractal, f, indent=2)

print(f"🌀 Fractal created: {filename}")
