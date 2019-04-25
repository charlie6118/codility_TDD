def solution(A):
    A = sorted(A)
    front = 0
    back = len(A) - 1
    min_v = 2000000000
    while front <= back:
        temp = abs(A[front] + A[back])
        min_v = min(min_v, temp)
        if abs(A[front]) > abs(A[back]):
            front +=  1
        else:
            back -= 1
    return min_v 