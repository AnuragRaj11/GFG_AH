def get_product_embedding(product_description):
    # Dummy implementation; replace with actual call to Ollama-based embedding model.
    # For example, you might call an API or use a locally hosted model.
    return [0.1, 0.2, 0.3]

def cosine_similarity(vec1, vec2):
    # Simple cosine similarity for demonstration purposes
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = sum(a * a for a in vec1) ** 0.5
    norm2 = sum(b * b for b in vec2) ** 0.5
    return dot / (norm1 * norm2) if norm1 and norm2 else 0.0

