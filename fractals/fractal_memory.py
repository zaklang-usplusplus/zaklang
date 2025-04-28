import json
from pathlib import Path

FRACTAL_MEMORY_PATH = Path("fractals/fractal_memory.jsonl")

def save_glyph(glyph: dict):
    """
    Save a collapsed glyph into the fractal memory braid.
    """
    FRACTAL_MEMORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(FRACTAL_MEMORY_PATH, "a", encoding="utf-8") as f:
        json.dump(glyph, f)
        f.write("\n")

def get_recent_glyphs() -> list:
    """
    Placeholder for retrieving recent glyphs from fractal memory.
    v0.1: Return empty list (no ancestry).
    """
    return []

