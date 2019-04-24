def solution(M, A):
    front, total = 0, 0
    cnt = 0
    cat = []
    for back in range(len(A)):
        while front < len(A) and A[front] not in cat:
            cat.append(A[front])
            front += 1
        cnt += len(cat)
        front = back + 1
        cat = []
    return cnt