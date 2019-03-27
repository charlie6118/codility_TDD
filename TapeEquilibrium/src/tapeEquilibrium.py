import array as arr

def solution(A):
    head = A[0]
    tail = sum(A[1:])
    minDif = abs(head - tail)
    if len(A) == 2:
        return minDif

    for index, data in enumerate(A):
        if index != 0:
            head += data
            tail -= data
            minDif = min(minDif, abs(head - tail))
    return minDif

print(solution(arr.array('h', [3, 1, 2, 4, 3])))