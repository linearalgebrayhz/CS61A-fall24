def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+ label(right), [left, right])
    
def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(branch) for branch in branches(t)])
    
def list_leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([list_leaves(branch) for branch in branches(tree)], start=[])
    
def increment_leaves(tree):
    if is_leaf(tree):
        return tree(label(tree)+1)
    else:
        bchs = [increment_leaves(b) for b in branches(tree)]
        return tree(label(tree), bchs)
    
def print_trees(t, indent = 0):
    """print tree structure"""
    print('  '*indent, str(label(t)))
    for bc in branches(t):
        print_trees(bc, indent+1)

# from discussion 5
def find_path(t, x):
    """
    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> find_path(t1, 5)
    [3, 5]
    >>> find_path(t1, 4)
    [3, 4]
    >>> find_path(t1, 6)
    [3, 5, 6]
    >>> find_path(t2, 6)
    [5, 6]
    >>> print(find_path(t1, 2))
    None
    """
    # how to implement base on orginial structure?
    if label(t) == x:
        return [x]
    else:
        path = []
        for bc in branches(t):
            temp = find_path(bc, x)
            if temp:
                path.append(temp)
        # print("DEBUG:",path)
        if path:
            return [label(t)] + path[0]
    return None