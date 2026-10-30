import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	
	g = np.array(gradient, dtype=float)
	magnitude = float(np.linalg.norm(g))

	if magnitude == 0:
		direction = np.zeros_like(g)
	else:
		direction = g / magnitude

	return {
        "magnitude": magnitude,
        "direction": direction.tolist(),
        "descent_direction": (-direction).tolist(),
    }
