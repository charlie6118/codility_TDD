def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(N, M):
    gcdValue = gcd(N, M)
    lcm = N * M // gcdValue
    return lcm // M

# def gcd(a, b, res):
#     if a == b:
#         print(a, b, res)
#         return b * res
#     elif a % 2 == 0 and b % 2 == 0:
#         return gcd(a // 2, b // 2, res * 2)
#     elif a % 2 == 0:
#         return gcd(a // 2, b, res)
#     elif b % 2 == 0:
#         return gcd(a, b // 2, res)
#     elif a > b:
#         return gcd(a - b, b, res)
#     else:
#         return gcd(a, b - a, res)