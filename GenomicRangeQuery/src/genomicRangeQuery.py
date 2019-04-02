from array import array

def solution(S, P, Q):
    rangeList = list(zip(P, Q))
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
    result = []
    print(intS)
    print(rangeList)
    for (start, last) in rangeList:
        print('S', start,'T', last)
        if start == last:
            result.append(intS[start])
        else:
            print(intS[0:2])
            result.append(min(intS[start:last+1]))
    return result



print(solution('CAGCCTA', array('b', [2, 5, 0]), array('b', [4, 5, 6])))