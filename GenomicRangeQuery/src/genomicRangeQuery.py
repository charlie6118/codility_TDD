from array import array

def solution(S, P, Q):
    rangeList = list(zip(P, Q))
    auxList = [[0, 0, 0, 0]] *(len(S) + 1) 

    intS = []
    for char in S:
        if char == 'A':
            intS.append(1)
        if char == 'C':
            intS.append(2)
        if char == 'G':
            intS.append(3)
        if char == 'T':
            intS.append(4)
    for index, char in enumerate(S):
        if char == 'A':
            auxList[index + 1] = [x + y for x, y in zip(auxList[index], [1, 0, 0, 0])]
        if char == 'C':
            auxList[index + 1] = [x + y for x, y in zip(auxList[index], [0, 1, 0, 0])]
        if char == 'G':
            auxList[index + 1] = [x + y for x, y in zip(auxList[index], [0, 0, 1, 0])]
        if char == 'T':
            auxList[index + 1] = [x + y for x, y in zip(auxList[index], [0, 0, 0, 1])]
    print(auxList)
    
    auxResult = []
    result = []
    for (start, last) in rangeList:
        auxResult.append([x - y for x, y in zip(auxList[last + 1], auxList[start])])

    print(auxResult)
    for r in auxResult:
        for index, e in enumerate(r):
            if e > 0:
                result.append(index + 1)
                break

    return result



print(solution('CAGCCTA', array('b', [2, 5, 0]), array('b', [4, 5, 6])))