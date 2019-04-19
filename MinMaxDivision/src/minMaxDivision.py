def blockValid(A, sum_candidate, allowed_chunks):
    block_cnt = 0
    current_sum = 0

    # if the current_sum exceed the allow_sum, cut the current_sum into block
    # and take element as current_sum
    for e in A:
        if current_sum + e > sum_candidate:
            current_sum = e
            block_cnt += 1
        else:
            current_sum += e
        # if block_cnt exceed the allow_chunks, return False
        if block_cnt >= allowed_chunks:
            return False
    return True

def solution(K, M, A):
    maxSum = sum(A)
    minSum = max(A)
    
    if K == 1: return maxSum
    if K > len(A): return minSum

    while minSum <= maxSum:
        sum_candidate = (minSum + maxSum) // 2
        # check if candidate is allowed with in K chunks, if Ture then modify the maxSum down, otherwise move the minSum up
        if blockValid(A, sum_candidate, K):
            maxSum = sum_candidate - 1
        else:
            minSum = sum_candidate + 1
    
    return minSum