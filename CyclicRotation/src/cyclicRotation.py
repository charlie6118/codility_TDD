import array as arr

def solution(A, K):
    if len(A) == 0:
        return A
    while K > 0:
        moveElement = A.pop()
        A.insert(0, moveElement)
        K-=1
    return A 
