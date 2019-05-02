def getHeight(subTree):
    if not subTree:
        return 0
    return max(getHeight(subTree.l), getHeight(subTree.r)) + 1

def solution(T):
    # write your code in Python 3.6
    if not T:
        return 0
    return max(getHeight(T.l), getHeight(T.r))