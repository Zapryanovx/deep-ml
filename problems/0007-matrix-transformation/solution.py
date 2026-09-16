import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A = np.array(A)
	T = np.array(T)
	S = np.array(S)
	
	if T.shape[0] != T.shape[1] or T.shape[0] != np.linalg.matrix_rank(T):
		return -1
	if S.shape[0] != S.shape[1] or S.shape[0] != np.linalg.matrix_rank(S):
		return -1

	if T.shape[1] != A.shape[0] or A.shape[1] != S.shape[0]:
		return -1

	T_inv = np.linalg.inv(T)
	return T_inv @ A @ S

	