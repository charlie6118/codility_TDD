import array as arr

def solution(A):
    lenOfArray = len(A)
    arraySum = 0
    arrayIdealSum = int((1 + lenOfArray) * lenOfArray / 2)
    checkIfNotPerm = {}

    for index in range(0, lenOfArray):
        if checkIfNotPerm.get(A[index], None) == None:
            checkIfNotPerm[A[index]] = 1
        elif checkIfNotPerm.get(A[index]) == 1:
            return 0
        checkIfNotPerm[A[index]] = 1
        arraySum += A[index]

    if arraySum == arrayIdealSum:
        return 1
    return 0

print(solution(arr.array('b', [4, 1, 3, 2])))

    # Error when sum correct but not in order     
    # total = len(A)
    # arrayIdealSum = (1 + total) * total / 2
    # if arrayIdealSum == sum(A):
    #     return 1
    # return 0 