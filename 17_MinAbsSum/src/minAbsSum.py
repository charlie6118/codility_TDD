def solution(A):
    lenA = len(A)
    for idx in range(lenA):
        A[idx] = abs(A[idx])
    
    sumA = sum(A)

    dp = [False] * (sumA + 1)
    dp[0] = True
    for i in range(lenA):
        for j in reversed(range(0, sumA + 1)):
            if dp[j] and dp[j + A[i]] <= sumA:
                dp[j + A[i]] = True

    min_v = sumA

    for i in range(sumA // 2 + 1):
        if dp[i] == 1:
            P = i
            Q = sumA - P
            min_v = min(min_v, Q - P)
    return min_v