from Trees import *

# numbers = tree(3, [tree(4), tree(5, [tree(6)])])

# haste = tree('h', [tree('a', [tree('s'), tree('t')]), tree('e')])

def print_sums(t, so_far):
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)

def count_path(t, total):
    """return the number of paths from the root to any node in tree t 
    for which the labels along the path sum to total."""
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_path(b, total=total - label(t)) for b in branches(t)])