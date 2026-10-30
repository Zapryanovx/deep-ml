import numpy as np

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    
    values, counts = np.unique(samples, return_counts=True)
    probs = counts / len(samples)

    return list(zip(values, probs))

    