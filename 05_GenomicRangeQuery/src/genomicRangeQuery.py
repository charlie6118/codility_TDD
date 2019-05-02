from array import array

def solution(S, P, Q):
    rangeList = list(zip(P, Q))
    auxList = [[0, 0, 0, 0]] *(len(S) + 1) 

    intS = []
    # Convert String to corresponding factor
    for char in S:
        if char == 'A':
            intS.append(1)
        if char == 'C':
            intS.append(2)
        if char == 'G':
            intS.append(3)
        if char == 'T':
            intS.append(4)
    # Count the nums of ACGT in each index of S
    for index, char in enumerate(S):
        if char == 'A':
            auxList[index + 1] = [x + y for x, y in zip(auxList[index], [1, 0, 0, 0])]
        if char == 'C':
            auxList[index + 1] = [x + y for x, y in zip(auxList[index], [0, 1, 0, 0])]
        if char == 'G':
            auxList[index + 1] = [x + y for x, y in zip(auxList[index], [0, 0, 1, 0])]
        if char == 'T':
            auxList[index + 1] = [x + y for x, y in zip(auxList[index], [0, 0, 0, 1])]
    
    auxResult = []
    result = []
    # Count the nums of ACGT in query ranges
    for (start, last) in rangeList:
        auxResult.append([x - y for x, y in zip(auxList[last + 1], auxList[start])])

    # If the small factor occurs, append it to the result
    for r in auxResult:
        for index, e in enumerate(r):
            if e > 0:
                result.append(index + 1)
                break

    return result