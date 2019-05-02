def solution(A):
    dp = [A[0]] * (len(A) + 6)
    # for i in range(1, len(A)):
    #     dp[i] = dp[i] + A[i]
    #     print(dp)
    for i in range(1, len(A)):
        dp[i + 6] = max(dp[i: i + 6]) + A[i]
    return dp[-1]