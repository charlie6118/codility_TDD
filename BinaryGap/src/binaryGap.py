def solution(N):
    binaryStr = '{:b}'.format(N)
    count = 0
    zeroList = binaryStr.split('1')
    if binaryStr[-1:] == '0':
        zeroList.pop()

    for zeroSet in zeroList:
        if len(zeroSet) > count:
            count = len(zeroSet)
    return count

    # count = 0
    # buffer = 0
    # findOne = False
    # for e in binaryStr:
    #     if e == '1' and findOne == False:
    #         findOne = True
    #     elif e == '1' and findOne == True:
    #         findOne = False
    #         if count < buffer:
    #             count = buffer
    #     if e == '0' and findOne == True:
    #         buffer += 1
    # return count