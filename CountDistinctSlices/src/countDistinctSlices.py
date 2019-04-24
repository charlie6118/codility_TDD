def solution(M, A):
    front, back = 0, 0
    cnt = 0
    lenA = len(A)
    seen = [False] * (M + 1)
    while front < lenA and back < lenA:
        while front < lenA and not seen[A[front]]:
            cnt += (front - back + 1)
            seen[A[front]] = True
            front += 1
        else:
            while front < lenA and back < lenA and A[front] != A[back]:
                seen[A[back]] = False
                back += 1
            seen[A[back]] = False
            back += 1
            
    return min(1000000000, cnt)