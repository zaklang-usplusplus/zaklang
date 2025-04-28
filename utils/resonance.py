import numpy as np

def calculate_resonance(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Calculate cosine similarity between two vectors.
    """
    dot_product = np.dot(vec1, vec2)
    norm_product = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    
    if norm_product == 0:
        return 0.0  # Avoid division by zero
    
    cosine_similarity = dot_product / norm_product
    normalized_similarity = (cosine_similarity + 1) / 2  # Normalize from [-1,1] to [0,1]
    
    return normalized_similarity
