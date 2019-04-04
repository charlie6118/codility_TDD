def solution(A):
    def tupleLength(t):
        return t[1] - t[0]

    rangeList = [(center - radius, center + radius) for center, radius in enumerate(A)]
    rangeList = sorted(rangeList, key = tupleLength, reverse = True)
    count = 0
    for i, (li, hi) in enumerate(rangeList):
        for j in range(i + 1, len(rangeList)):
            if li != hi and rangeList[j][0] != rangeList[j][1]:
                if (rangeList[j][0] < li and rangeList[j][1] < hi and not (rangeList[j][1] < li)) or (rangeList[j][0] > li and rangeList[j][1] > hi and not(rangeList[j][0] > hi)):
                    count += 1
                elif (rangeList[j][0] < li and rangeList[j][1] == hi) or (rangeList[j][0] > li and rangeList[j][1] == hi):
                    count += 1
                elif (rangeList[j][0] == li and rangeList[j][1] < hi) or (rangeList[j][0] == li and rangeList[j][1] > hi):
                    count += 1
                elif (rangeList[j][0] > li and rangeList[j][1] < hi) or (rangeList[j][0] < li and rangeList[j][1] > hi):
                    count +=1
                else:
                    continue
            else:
                if hi == li:
                    if rangeList[j][0] <= hi <= rangeList[j][1]:
                        count += 1
                if rangeList[j][0] == rangeList[j][1]:
                    if li <= rangeList[j][0] <= hi:
                        count += 1
    return count
solution([1, 5, 2, 1, 4, 0])