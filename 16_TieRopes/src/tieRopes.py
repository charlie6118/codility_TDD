def solution(K, A):
    lenA = len(A)
    cnt = 0
    acc = 0
    for e in A:
        acc += e
        if acc >= K:
            cnt += 1
            acc = 0

    return cnt