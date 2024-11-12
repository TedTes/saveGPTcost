import numpy as np

def get_similarity_score(embedding1, embedding2):
    embedding1 = embedding1.cpu().numpy() if hasattr(embedding1, 'cpu') else embedding1
    embedding2 = embedding2.cpu().numpy() if hasattr(embedding2, 'cpu') else embedding2
    return np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))