def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0]) != len(b):
		return -1
		
	dot_product = []
	for row in a:
		cell = 0
		for col in range(0, len(row)):
			cell += row[col] * b[col]
		dot_product.append(cell)
	return dot_product