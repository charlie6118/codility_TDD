import array as arr

def solution(N, A):
    counters = [0] * N
    def increase(counters, X):
        counters[X] += 1
        return counters
    def maxCounters(counters):
        maxCounter = max(counters)
        return [maxCounter] * N

    for _, value in enumerate(A):
        if 1 <= value <= N:
            counters = increase(counters, value - 1)
        if value == N + 1:
            counters = maxCounters(counters)
    return counters
        
print(solution(5, arr.array('b', [3, 4, 4, 6, 1, 4, 4])))