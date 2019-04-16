def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def hasSameFactor(a, b):
    gcdValue = gcd(a, b)
    while a != 1:
        gcd_a = gcd(a, gcdValue)
        if gcd_a == 1:
            break
        a = a // gcd_a
    else:
        while b != 1:
            gcd_b = gcd(b, gcdValue)
            if gcd_b == 1:
                break
            b = b // gcd_b
        else:
            return True
    return False

def solution(A, B):
    cnt = 0
    for a, b in zip(A, B):
        if hasSameFactor(a, b):
            cnt += 1
    return cnt

