def search(f):
    x = 0
    while not f(x):
        x += 1
    return x

def square(x):
    return x * x

def inverse(f):
    """Find g such that g(f(x)) -> x"""
    return lambda y: search(lambda x: f(x) == y)

# newton's method?