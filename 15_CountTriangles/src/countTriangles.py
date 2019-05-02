def solution(A):
    A = sorted(A)
    tri_cnt = 0
    for first in range(len(A) - 2):
        second = first + 1
        third = first + 2
        while third < len(A):
            if A[first] + A[second] > A[third]:
                tri_cnt += third - second
                third += 1
            elif second < third - 1:
                second += 1
            else:
                second += 1
                third += 1
    return tri_cnt