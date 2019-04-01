import array as arr

def solution(N, A):
    # credit. Andrei Simionescu 

    counters = [0] * N
    finalMax = 0
    maxAfterOper = 0

    for _, value in enumerate(A):
        value -= 1
        if value == N:
            finalMax = maxAfterOper
            continue 
        if 0 <= value < N:
            counters[value] = max(counters[value], finalMax) + 1
            maxAfterOper = max(counters[value], maxAfterOper)

    for index in range(N):
        counters[index] = max(counters[index], finalMax)

    return counters

    # counters = [0] * N
    # def increase(counters, X):
    #     counters[X] += 1
    #     return counters
    # def maxCounters(counters):
    #     maxCounter = max(counters)
    #     return [maxCounter] * N

    # for _, value in enumerate(A):
    #     if 1 <= value <= N:
    #         counters = increase(counters, value - 1)
    #     if value == N + 1:
    ##########this is being consider as O(n*m)##########
    #         counters = maxCounters(counters)
    # return counters

print(solution(5, arr.array('b', [3, 4, 4, 6, 1, 4, 4])))