def solution(X, Y, D):
    if X == Y:
        return 0
    result = abs(Y-X) / D
    if result > round(result):
        return round(result) + 1
    return round(result)