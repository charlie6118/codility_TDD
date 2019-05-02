def solution(A, B, K):
    last = (B // K)
    start = (A // K)
    r = 1 if A % K == 0 else 0
    return last - start + r