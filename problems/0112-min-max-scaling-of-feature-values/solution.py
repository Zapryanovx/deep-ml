import numpy as np

def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """

    x = np.array(x)
    if min(x) == max(x):
        return [0.0] * len(x)
    return ((x - min(x)) / (max(x) - min(x))).tolist()