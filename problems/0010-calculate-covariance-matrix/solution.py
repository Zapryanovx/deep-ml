import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	X = np.array(vectors)
	n = X.shape[1]

	mean_cols = np.mean(X, axis=1, keepdims=True)
	X_centered = X - mean_cols

	cov = (X_centered @ X_centered.T) / (n - 1)
	return cov.tolist()