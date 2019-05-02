def solution(A):
    stack = []
    for e in A:
        stack.append(e)
        if len(stack) > 1:
            if stack[-1] != stack[-2]:
                print('loop 1')
                stack.pop()
                stack.pop()
    if len(stack) > 0:
        count = 0
        dominator = stack[0]
        for index in range(len(A)):
            if A[index] == dominator:
                count += 1
        if count > (len(A) //2):
            pass
    if len(stack) == 0:
        return 0
    equiCounter = 0
    leftCounter = 0
    for index, value in enumerate(A):
        if value == dominator:
            leftCounter += 1
        if leftCounter > (index + 1) // 2 and (count - leftCounter) > (len(A) - (index + 1)) // 2:
            equiCounter += 1
    return equiCounter