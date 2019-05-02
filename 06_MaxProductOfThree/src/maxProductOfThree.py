def solution(A):
    if len(A) == 3:
        return A[0] * A[1] * A[2]

    plus = sorted([n for n in A if n > 0])
    minus = sorted([n for n in A if n < 0])
    
    # ---
    if len(plus) == 0:
        if 0 not in A:
            return minus[len(minus) - 1] * minus[len(minus) - 2] * minus[len(minus) - 3]
        else:
            return 0
    
    # +++
    ppp = -1000000
    if len(plus) > 2:
        ppp = plus[len(plus) - 1] * plus[len(plus) - 2] * plus[len(plus) - 3]
    # --+
    mmp = -1000000
    if len(minus) > 1 and len(plus) > 0:
        mmp = plus[len(plus) - 1] * minus[0] * minus[1]

    return max(ppp, mmp)

print(solution([-3, 1, 2, -2, 5, 6]))