import array as arr

def solution(X, A):

    allNeedPath = list(range(1, X + 1))

    for index, value in enumerate(A):
        try:
            allNeedPath.remove(value)
        except:
            pass
        if len(allNeedPath) == 0:
            return index
    return -1

print(solution(5, arr.array('b', [1, 3, 1, 4, 2, 3, 5, 4])))