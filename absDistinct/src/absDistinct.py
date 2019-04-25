def solution(A):
    seen = set()
    for e in A:
        e = abs(e)
        seen.add(e)
    return len(seen)