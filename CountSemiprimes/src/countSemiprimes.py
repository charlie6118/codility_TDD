def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while i * i <= n:
        if sieve[i]:
            k = i * i
            print(k)
            while(k <= n):
                sieve[k] = False
                k += i
        i += 1
    return sieve
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def arrayF(N):
    F = [0] * (N + 1)
    i = 2
    while i * i <= N:
        if F[i] == 0:
            k = i * i
            while k <= N:
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1
    return F

def solution(N, P, Q):
    # write your code in Python 3.6
    f = arrayF(N)
    prefixSum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefixSum[i] = prefixSum[i - 1]
        if f[i] != 0:
            first_factor = f[i]
            secont_factor = int(i / first_factor)
            if f[first_factor] == 0 and f[secont_factor] == 0:
                prefixSum[i] += 1
    result = []
    for i in range(len(Q)):
        result.append(prefixSum[Q[i]] - prefixSum[P[i] - 1])
    return result

def factorization(x, F):
    primeFactors = []
    while (F[x] > 0):
        print(x, F[x])
        primeFactors += [F[x]]
        print(primeFactors)
        x = x // F[x]
    primeFactors += [x]
    return primeFactors