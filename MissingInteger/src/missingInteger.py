from array import array

def solution(A):
    space = [0] * (len(A) + 1)
    
    for value in A:
        if 0 < value <= len(A):
            space[value - 1] += 1
    
    for index, value in enumerate(space):
        if value == 0:
            return index + 1

print(solution(array('b', [1, 2, 3])))