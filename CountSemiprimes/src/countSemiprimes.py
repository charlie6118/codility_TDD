# get min_prime for each single integer
def getMinPrimeForEachInteger(N):
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
    f = getMinPrimeForEachInteger(N)
    prefixSum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefixSum[i] = prefixSum[i - 1]
        # count increase when first_factor exist and corresponding index of second_factor in f is zero
        if f[i] != 0:
            first_factor = f[i]
            second_factor = (i // first_factor)
            if f[second_factor] == 0:
                prefixSum[i] += 1
                
    result = []
    for i in range(len(Q)):
        result.append(prefixSum[Q[i]] - prefixSum[P[i] - 1])
    return result

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


def factorization(x, F):
    primeFactors = []
    while (F[x] > 0):
        print(x, F[x])
        primeFactors += [F[x]]
        print(primeFactors)
        x = x // F[x]
    primeFactors += [x]
    return primeFactors