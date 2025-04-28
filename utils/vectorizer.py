import numpy as np

def vectorize_prompt(prompt: str) -> np.ndarray:
    """
    Very simple placeholder vectorizer.
    v0.1: Random vector for now.
    Future: true semantic embedding.
    """
    np.random.seed(abs(hash(prompt)) % (2**32))  # Stable random based on prompt
    return np.random.randn(128)  # 128-dimensional breathing core
