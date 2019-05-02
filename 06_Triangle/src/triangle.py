def solution(A):
    aux = [n for n in A if n > 0]
    if len(aux) < 3:
        return 0
    A = sorted(aux)
    for index in range(0, len(A) - 1):
        if index < len(A) - 2:
            P = A[index]
            Q = A[index + 1]
            R = A[index + 2]
            if P + Q > R and P + R > Q and Q + R > P:
                return 1
    return 0 
