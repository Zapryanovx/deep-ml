import numpy as np

def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""

	data = np.arange(1, n + 1)

	mean = float(np.mean(data))
	variance = float(np.round(np.var(data), 4))

	return (mean, variance)