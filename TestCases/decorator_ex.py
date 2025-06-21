def trace1(fn):
    """returns a print version of function

    fn - a function to be decorated
    """
    def traced(x):
        print("Calling", fn, "with argument", x)
        return fn(x)
    
    return traced

@trace1
def square(x):
    return x*x

# This is equivalent to
"""
def square(x):
    return x * x
square = trace1(square)
"""


@trace1
def sum_squares_up_to(n):
    total = 0
    for i in range(1, n+1):
        total += square(i)
    return total