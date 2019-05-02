import math

def solution(A, B):
    F = [0] * (max(A) + 2)
    F[1] = 1
    result = []
    for i in range(2, max(A) + 2):
        if F[i] == 0:
            F[i] = F[i - 1] + F[i - 2]

    for i in range(len(A)):
        result.append(F[A[i] + 1] % pow(2, B[i]))
    
    return result

