import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""

	A = A.astype(float).copy()
	b = b.astype(float).copy()
	n = len(b)

	for k in range(n):
		p = k + np.argmax(np.abs(A[k:, k]))
		A[[k, p]] = A[[p, k]]
		b[[k, p]] = b[[p, k]]

		for i in range(k + 1, n):
			factor = A[i, k] / A[k, k]
			A[i] -= factor * A[k]
			b[i] -= factor * b[k]

	x = np.zeros(n)
	for i in range(n - 1, -1, -1):
		x[i] = (b[i] - A[i, i+1:] @ x[i+1:]) / A[i, i]

	return x
