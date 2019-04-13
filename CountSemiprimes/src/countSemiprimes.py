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

def sieveNums(n):
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
    sieve_nums = []
    for index in range(len(sieve)):
        if sieve[index] == True:
            sieve_nums.append(index)
    return sieve_nums

def getRange(P, Q):
    range_pair = []
    for index in range(len(P)):
        range_pair.append((P[index], Q[index]))
    return (range_pair)

def getSemiprimes(N, P, Q):
    sieve_nums = sieveNums(max(Q))
    semiprimes = set()
    for i in range(len(sieve_nums)):
        for j in range(i, len(sieve_nums)):
            if sieve_nums[i] * sieve_nums[j] > N:
                break
            semiprimes.add(sieve_nums[i] * sieve_nums[j])
    return list(semiprimes)

def solution(N, P, Q):
    range_pair = getRange(P, Q)
    semiprimes = getSemiprimes(N, P, Q)
    result = []
    for (p, q) in range_pair:
        count = 0
        for semiprime in semiprimes:
            if p <= semiprime <= q:
                count += 1
        result.append(count)
        count == 0
    return result

def arrayF(n):
    F = [0] * (n + 1)
    i = 2
    while i * i <= n:
        if F[i] == 0:
            k = i * i
            while k <= n:
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1
    return F

def factorization(x, F):
    primeFactors = []
    while F[x] > 0:
        primeFactors += [F[x]]
        x /= F[x]
    primeFactors += [x]
    return primeFactors

print(sieve(17))
print(arrayF(20))
print(factorization(19, arrayF(20)))