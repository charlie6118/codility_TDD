def solution(A):
    fromOne = [0] * len(A)
    fromLast = [0] * len(A)

    for i in range(1, len(A)):
        fromOne[i] = max(0, fromOne[i - 1] + A[i])

    for i in reversed(range(len(A) - 1)):
        fromLast[i] = max(0, fromLast[i + 1] + A[i])

    print(fromOne)
    print(fromLast)
    result = 0
    for i in range(1, len(A) - 1):
        result = max(result, fromOne[i - 1] + fromLast[i + 1])
    return result

solution([3, 2, 6, -1, 4, 5, -1, 2])