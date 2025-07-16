"""
From discussion 8, Q4
"""
from Link import Link

def display(s, k=10):
    """Print the first k digits of infinite linked list s as a decimal.

    >>> s = Link(0, Link(8, Link(3)))
    >>> s.rest.rest.rest = s.rest.rest
    >>> display(s)
    0.8333333333...
    """
    assert s.first == 0, f'{s.first} is not 0'
    digits = f'{s.first}.'
    s = s.rest
    for _ in range(k):
        assert s.first >= 0 and s.first < 10, f'{s.first} is not a digit'
        digits += str(s.first)
        s = s.rest
    print(digits + '...')


def divide(n, d):
    """Return a linked list with a cycle containing the digits of n/d.

    >>> display(divide(5, 6))
    0.8333333333...
    >>> display(divide(2, 7))
    0.2857142857...
    >>> display(divide(1, 2500))
    0.0004000000...
    >>> display(divide(3, 11))
    0.2727272727...
    >>> display(divide(3, 99))
    0.0303030303...
    >>> display(divide(2, 31), 50)
    0.06451612903225806451612903225806451612903225806451...
    """
    assert n > 0 and n < d
    result = Link(0)  # The zero before the decimal point
    "*** YOUR CODE HERE ***"
    tail = result
    res_digits = {}
    while True:
        quo, res = (n * 10) // d, (n * 10) % d
        pair = (quo, res)
        if res == 0:
            tail.rest = Link(quo)
            new_node = Link(0)
            tail.rest.rest = new_node
            tail.rest.rest.rest = new_node
            break
        if pair in res_digits:
            tail.rest = res_digits[pair]
            break
        else:
            new_node = Link(quo)
            res_digits[pair] = new_node
            tail.rest = new_node
            tail = tail.rest
        
        n = res

    return result

"""
Neither quo nor res is unique!
For test case one:
5 / 6
quo 8 res 2 <-- replicated res
quo 3 res 2 <-- replicated res
quo 3 res 2
...
"""
