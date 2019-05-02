def solution(A):
    # write your code in Python 3.6
    n = len(A)
    d = {}
    i_sum = (n + 1) * n // 2
    
    for e in A:
        d[e] = d.get(e, 0) + 1
        if d[e] > 1:
            return 0
    if i_sum == sum(A):
        return 1
    return 0