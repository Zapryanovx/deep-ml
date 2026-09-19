def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """

    encoded_order = dict(zip(order, range(len(order))))
    encoded_values = []

    for v in values:
        encoded_values.append(encoded_order.get(v, -1))

    return encoded_values
