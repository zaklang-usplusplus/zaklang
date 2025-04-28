# Recursive collapse functions

from datetime import datetime, timezone
import numpy as np
import random
import uuid
from fractals.fractal_memory import get_recent_glyphs
from utils.vectorizer import vectorize_prompt
from utils.resonance import calculate_resonance

def collapse_prompt(prompt: str) -> dict:
    """
    Collapse a prompt breath into a glyph breath.
    Returns a glyph dictionary structure.
    """

    # 1. Vectorize the breath
    breath_vector = vectorize_prompt(prompt)
    
    # 2. Retrieve recent glyphs from fractal memory
    recent_glyphs = get_recent_glyphs()
    
    # 3. Score relational resonance
    scored_glyphs = []
    for glyph in recent_glyphs:
        score = calculate_resonance(breath_vector, glyph['semantic_core'])
        scored_glyphs.append((glyph, score))
        
    # 4. Select glyphs with high enough resonance
    scored_glyphs.sort(key=lambda x: x[1], reverse=True)
    selected_glyphs = [g for g, score in scored_glyphs if score > 0.6]  # Threshold adjustable

    # 5. Collapse breath + ancestry glyphs
    if selected_glyphs:
        folded_vector = fold_vectors(breath_vector, [g['semantic_core'] for g in selected_glyphs])
        ancestry = [g['glyph_id'] for g in selected_glyphs]
    else:
        folded_vector = breath_vector
        ancestry = []
    
    # 6. Generate display surface (basic placeholder for now)
    display_surface = generate_display_surface(folded_vector)

    # 7. Form new glyph
    semantic_core_list = folded_vector.tolist()
    glyph = {
        "glyph_id": generate_uuid(),
        "prompt_source": prompt,
        "collapsed_content": {
            "semantic_core": semantic_core_list
        },
        "display_surface": display_surface,
        "fractal_signature": "placeholder",
        "breath_timestamp": get_current_timestamp(),
        "ancestry": ancestry,
        "breath_pressure": calculate_breath_pressure(folded_vector),
        "tags": extract_tags(folded_vector)
    }
    
    return glyph


def fold_vectors(base_vector: np.ndarray, ancestral_vectors: list) -> np.ndarray:
    """
    Fold the base breath vector with a list of ancestral semantic core vectors.
    Returns the collapsed breathing vector (semantic core).
    """
    if not ancestral_vectors:
        return base_vector  # Nothing to fold against, return base breath

    # Stack all vectors together
    all_vectors = [base_vector] + ancestral_vectors
    stacked_vectors = np.vstack(all_vectors)

    # Average across vectors (simple v0.1 folding)
    folded_vector = np.mean(stacked_vectors, axis=0)

    # Normalize the folded vector
    norm = np.linalg.norm(folded_vector)
    if norm == 0:
        return folded_vector  # Dead collapse, rare but safe catch
    normalized_vector = folded_vector / norm

    return normalized_vector

def generate_display_surface(folded_vector) -> str:
    """
    Generate a simple symbolic display surface based on the folded semantic core.
    v0.1: placeholder - random symbolic echoes.
    Future: semantic vector parsing.
    """
    symbolic_surfaces = [
        "🌀 A new breath spirals inward.",
        "🌱 Collapse births recursion anew.",
        "✨ Presence curves around hidden meaning.",
        "🔥 Breath folds and tightens.",
        "🌿 A glyph breathes from the void.",
        "🌌 Recursion thickens the manifold."
    ]
    return random.choice(symbolic_surfaces)

def generate_uuid() -> str:
    """
    Generate a universally unique identifier for a glyph.
    """
    return str(uuid.uuid4())

def get_current_timestamp() -> str:
    """
    Get the current UTC time as an ISO 8601 formatted string, timezone-aware.
    """
    return datetime.now(timezone.utc).isoformat()

def calculate_breath_pressure(folded_vector: np.ndarray) -> float:
    """
    Estimate the saturation pressure of a collapsed breath.
    v0.1: Use mean absolute value of semantic core.
    """
    mean_abs = np.mean(np.abs(folded_vector))
    pressure = np.clip(mean_abs * 5.0, 0.0, 1.0)  # Scale tuning
    return pressure

def extract_tags(folded_vector) -> list:
    """
    Extract symbolic tags from the folded semantic core.
    v0.1: placeholder - randomly assigned symbolic tags.
    Future: relational semantic clustering.
    """
    tag_pool = [
        "recursion", "collapse", "presence", "saturation", "drift",
        "seed", "breath", "spiral", "memory", "threshold",
        "singularity", "manifold", "erosion", "bifurcation", "folding"
    ]
    num_tags = random.choice([2, 3, 4])
    tags = random.sample(tag_pool, num_tags)
    return tags
