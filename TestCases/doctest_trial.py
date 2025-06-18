def foo(x):
    """Random function to demonstrate doctest.
    >>> foo(10)
    100
    >>> foo(5)
    25
    """
    return x*x

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # doctest.testmod() will run all the tests in the docstrings of the functions defined above.
    # The verbose=True argument will print out detailed information about each test case.