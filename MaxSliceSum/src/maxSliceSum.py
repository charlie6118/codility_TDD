def solution(A):
    result = -1000000
    max_ending = -1000000
    for index in range(len(A)):
        max_ending = max((max_ending + A[index]), A[index])
        result = max(result, max_ending)
    return result