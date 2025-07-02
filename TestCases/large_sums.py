def large(s, n):
    if s == []:
        return []
    elif s[0] > n:
        return large(s[1:], n)
    else:
        first = s[0]
        with_s0 = [first] + large(s[1:], n-first)
        without_s0 = large(s[1:], n)
        if sum(with_s0) > sum(without_s0):
            return with_s0
        else:
            return without_s0