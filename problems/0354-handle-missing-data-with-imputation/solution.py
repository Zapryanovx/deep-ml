import numpy as np

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
        
    Returns:
        2D numpy array with missing values imputed
    """

    result = np.array(data, dtype=float)

    for j in range(result.shape[1]):
        column = result[:, j]
        missing = np.isnan(column)
        present = column[~missing]

        if present.size == 0:
            continue

        value = -1
        if strategy == 'mean':
            value = present.mean()
        elif strategy == 'median':
            value = np.median(present)
        elif strategy == 'mode':
            values, counts = np.unique(present, return_counts=True)
            value = values[np.argmax(counts)]    
        else:
            raise ValueError(f"Unknown strategy: {strategy}")

        column[missing] = value

    return result
