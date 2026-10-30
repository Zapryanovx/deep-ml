import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """

    data = np.array(data)

    mean = float(np.mean(data))
    median = float(np.median(data))

    values, counts = np.unique(data, return_counts=True)
    mode = values[np.argmax(counts)].item()

    variance = float(np.round(np.var(data), 4))
    std_dev = float(np.round(np.std(data), 4))

    p25, p50, p75 = np.percentile(data, [25, 50, 75])
    iqr = float(p75 - p25)

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": std_dev,
        "25th_percentile": float(p25),
        "50th_percentile": float(p50),
        "75th_percentile": float(p75),
        "interquartile_range": iqr,
    }
