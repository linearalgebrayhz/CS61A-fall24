def count_partition(n, m):
    """ count partition of n by numbers less than m

    >>> count_partition(6, 4)
    9

    """
    if n == 0:
        return 1
    elif n < 0 or m == 0:
        return 0    
    else:
        with_m = count_partition(n-m, m)
        without_m = count_partition(n, m-1)
        return with_m + without_m
    
# a refined version
def count_partition_refined(n, m):
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = count_partition_refined(n-m, m)
        without_m = count_partition_refined(n, m-1)
        return exact_match + with_m + without_m

def list_partition(n, m):
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [p + [m] for p in list_partition(n-m, m)]
        without_m = list_partition(n, m-1)
        return exact_match + with_m + without_m

def string_partition(n, m):
    if n < 0 or m == 0:
        return []
    else: 
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + " + " +  str(m) for p in string_partition(n-m, m)]
        without_m = string_partition(n, m-1)
        return exact_match + with_m + without_m

# fast to look at first few samples!!
def yield_partition(n, m):
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in string_partition(n-m, m):
            yield p + ' + ' + str(m)
        yield from yield_partition(n, m - 1)

    
if __name__ == "__main__":
    for p in string_partition(6,4):
        print(p)