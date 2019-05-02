def solution(A):
    result = 0
    target = 200000
    for index in range(len(A)):
        target = min(target, A[index])
        result = max((A[index] - target), result)
    return result