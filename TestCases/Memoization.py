def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

if __name__ == "__main__":
    fib = count(fib)
    counted_fib = fib
    fib = memo(fib)
    fib = count(fib)
    fib(30)
    print(fib.call_count)
    print(counted_fib.call_count)