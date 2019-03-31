def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)
    print(count)
    print(type(count))

    for k in range(0, n):
        count[A[k] -1] += 1
    return count

print(counting([3, 4, 2], 3))