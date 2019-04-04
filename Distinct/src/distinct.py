def solution(A):
    auxSet = set()
    for e in A:
        auxSet.add(e)
    return len(auxSet)