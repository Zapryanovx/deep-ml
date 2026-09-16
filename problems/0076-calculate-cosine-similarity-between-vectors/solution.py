import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	
	dot_product = v1 @ v2
	norm_v1 = np.linalg.norm(v1)
	norm_v2 = np.linalg.norm(v2)

	if norm_v1 == 0 or norm_v2 == 0:
		return 0.0
	return float(dot_product / (norm_v1 * norm_v2))
