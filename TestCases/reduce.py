from operator import add, mul, truediv

def reduce(f, s, initial):
    """
    >>> reduce(mul, [1, 2, 3], 1)
    6
    """
    for elem in s:
        initial = f(initial, elem)
    return initial

def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')