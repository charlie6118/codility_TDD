from array import array

def solution(A):

    counters = 0
    aux = 0

    for index in range(len(A)):
        if A[index] == 1:
            counters += aux
        else:
            aux += 1
        if counters > 1E9:
            return -1
    return counters

    # lenOfArray = len(array)
    # pairList = []
    # for index, value in enumerate(array):
    #     print(index, value)
    #     if value == 0:
    #         for j in range(index + 1, lenOfArray):
    #             if array[j] == 1:
    #                 pairList.append((index, j))
    #     if value == 1:
    #         for j in range(0, index):
    #             print(j)
    #             if array[j] == 0:
    #                 pairList.append((index, j))

    # print(pairList)
    # return int(len(pairList)/2)

solution(array('b', [0, 1, 0, 1, 1]))