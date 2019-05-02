def solution(A, B):
    # write your code in Python 3.6
    if len(A) == 0: return 0
    cnt = 1
    tail = B[0]
    for i in range(1, len(A)):
        if A[i] > tail:
            cnt += 1
            tail = B[i]
    return cnt