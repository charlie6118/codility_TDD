def solution(N):
    binaryStr = '{:b}'.format(N)
    count = 0
    zeroLists = binaryStr.split('1')
    if binaryStr[-1] == '0':
        zeroLists.pop()

    for zeroList in zeroLists:
        if len(zeroList) > count:
            count = len(zeroList)
    return count