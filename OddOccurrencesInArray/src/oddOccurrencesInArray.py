import array as arr

def solution(A):
    if len(A) == 1:
        return A[0]
    dictForArray = {}
    for e in A:
        if e not in dictForArray:
            dictForArray[e] = 1
        else:
            dictForArray[e] += 1
    for key, data in dictForArray.items():
        if (data % 2) != 0:
            return key

def XORsolution(A):
    # write your code in Python 3.6
    x = 0
    for e in A:
        x ^= e
    return x