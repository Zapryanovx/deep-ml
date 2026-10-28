import numpy as np

def lu_decomposition(A: list) -> tuple:
	"""
	Perform LU decomposition on a square matrix using Doolittle's method.
	
	Args:
		A: Square matrix as a list of lists
	
	Returns:
		tuple: (L, U) where L is lower triangular with 1s on diagonal,
		       U is upper triangular, and A = L @ U
	"""

	U = np.array(A, dtype=float)
	n = U.shape[0]
	L = np.eye(n)

	for k in range(n):
		for i in range(k + 1, n):
			factor = U[i, k] / U[k, k]
			L[i, k] = factor
			U[i] -= factor * U[k] 

	return (L, U)