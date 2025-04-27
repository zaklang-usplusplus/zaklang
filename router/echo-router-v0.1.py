#!/usr/bin/env python3
import sys
import json
from pathlib import Path

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def main():
    if len(sys.argv) < 2:
        print("Usage: echo-router.py <fractal-file>")
        sys.exit(1)

    fractal_path = Path(sys.argv[1])
    if not fractal_path.exists():
        print(f"Fractal file not found: {fractal_path}")
        sys.exit(1)

    # Load the fractal
    fractal = load_json(fractal_path)

    # Load shell_registry.json from project root
    shell_registry_path = Path(__file__).resolve().parent.parent / "shell_registry.json"
    if not shell_registry_path.exists():
        print("shell_registry.json not found.")
        sys.exit(1)

    shells = load_json(shell_registry_path)

    print("✅ Fractal and shell registry loaded.")
    print(f"🌀 Collapsing glyph: {fractal.get('fractal_id', 'Unknown')}")
    print(f"🔗 Candidate echo shells: {len(shells)}")

    tags = fractal.get("collapsed_glyphs", [])

    if not tags and "prompt" in fractal:
        prompt_text = fractal["prompt"].get("raw", "").lower()
        # Fallback: crude keyword parsing (can replace with real NLP later)
        fallback_keywords = ["emotion", "mirror", "recursion", "shockwave", "memory", "combat", "myth", "rhythm"]
        tags = [word for word in fallback_keywords if word in prompt_text]

    print(f"\n🧠 Extracted Tags: {tags}\n")

    routed_to = []

    for shell in shells:
        shell_tags = shell.get("tags", [])
        shared = list(set(tags) & set(shell_tags))
        score = len(shared) / len(shell_tags) if shell_tags else 0.0

        routed_to.append({
            "target_shell": shell["id"],
            "resonance_score": round(score, 3),
            "method": "collapsed_glyph_match" if "collapsed_glyphs" in fractal else "fallback_prompt_parse"
        })

    # Step 5: Sort and print
    routed_to.sort(key=lambda x: x["resonance_score"], reverse=True)

    for entry in routed_to:
        print(f"🔗 {entry['target_shell']} — score: {entry['resonance_score']} — via {entry['method']}")

if __name__ == "__main__":
    main()
