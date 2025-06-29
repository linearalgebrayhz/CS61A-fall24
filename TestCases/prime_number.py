"""
From discussion 3, Q3

"""

def is_prime(n):
    assert n > 1
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True

# Not efficient, just demonstrating recursion
def is_prime_recursive(n):
    assert n > 1

    def helper(factor):
        if factor == n:
            return True
        if n % factor == 0:
            return False
        return helper(factor + 1)
    
    return helper(2)