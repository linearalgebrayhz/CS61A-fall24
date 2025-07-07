def even(start, end):
    start = start + (start % 2)
    while start < end:
        yield start
        start += 2

def a_then_b(a, b):
    """yield from statement yields all values from an iterator or iterable"""
    yield from a
    yield from b

def count_down(k):
    if k > 0:
        yield k
        # yield count_down would not work. Because the return value would be an iterator obj
        # or yield from
        for i in count_down(k-1):
            yield i

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])

if __name__ == "__main__":
    t = even(1,10)
    print(next(t))
    print(next(t))
    print(next(t))
    print(list(a_then_b([1, 2], [3, 4])))