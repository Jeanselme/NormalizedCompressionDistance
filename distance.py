import lz4.frame as compressor # Use lzma for shorter array

def ncd(x, y):
    """
        Computes distance between x and y

        Args:
            x (numpy array): Object 1
            y (numpy array): Object 2

        Returns:
            Distance between objects
    """
    # Obtain bytes
    x_str, y_str = x.tobytes(), y.tobytes()

    # Compute compression
    x_compession = len(compressor.compress(x_str))
    y_compession = len(compressor.compress(y_str))
    xy_compession = len(compressor.compress(x_str + y_str))

    # Compute distance
    return (xy_compession - min(x_compession, y_compession)) / max(x_compession, y_compession)


