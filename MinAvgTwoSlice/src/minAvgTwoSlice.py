def solution(A):
    minValue = 10001
    minIndex = len(A)

    if minIndex == 2:
        return 0
        
    for index in range(0, len(A) - 1):
        if index < len(A) - 1:
            tempPair = (A[index] + A[index + 1]) / 2.0
        else: tempPair = 10001
        if index < len(A) - 2:
            tempTripple = (A[index] + A[index + 1] + A[index + 2]) / 3.0
        else: tempTripple = 10001

        if tempPair < minValue:
            minValue = tempPair
            minIndex = index
        if tempTripple < minValue:
            minValue = tempTripple
            minIndex = index

    return minIndex

print(solution([-3, -5, -8, -4, -10]))