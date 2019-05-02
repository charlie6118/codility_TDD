def solution(A):
    right = sum(A[1:])
    left = A[0]
    min_v = abs(right - left)
    for i in range(1, len(A) - 1):
        left += A[i]
        right -= A[i]
        min_v = min(min_v, abs(right - left))
    return min_v