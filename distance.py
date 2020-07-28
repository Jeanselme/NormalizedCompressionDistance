import lz4.frame as compressor # Use lzma for shorter array

def ncd(x, y, symmetric = True, concatenate = lambda x, y: np.concatenate([x, y])):
    """
        Computes distance between x and y

        Args:
            x (numpy array): Object 1
            y (numpy array): Object 2

            symmetric (bool): Enforce symmetry (slower)
            concatenate (func): Concatenation function

        Returns:
            Distance between objects
    """
    # Compute compression
    x_compession = len(compressor.compress(x))
    y_compession = len(compressor.compress(y))
    xy_compession = len(compressor.compress(concatenate(x, y)))

    # Ensure symmetry for fast compression
    if symmetric:
        xy_compession = min(xy_compession, len(compressor.compress(concatenate(y, x))))

    # Compute distance
    return (xy_compession - min(x_compession, y_compession)) / max(x_compession, y_compession)