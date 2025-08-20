def square(x: int, /) -> int:
    """Return the square of x.

    This function is here to demonstrate how `doctest` works.

    Args:
        x: The number to square.

    Returns:
        The square of x.

    Example:
        >>> square(3)
        9
        >>> square(-4)
        16
        >>> square(0)
        0
    """
    return x**2
