import array as arr

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def solution(A):
    N = len(A) + 1
    Sum = (1 + N) * N / 2
    return round(Sum) - sum(A)

    # if len(A) == 0:
    #     return 1
    # if len(A) == 1:
    #     return 2
    # A = bubbleSort(A)
    # for index, value in enumerate(A):
    #     if (index + 1) != value:
    #         return index + 1
    # return len(A) + 1