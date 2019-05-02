def solution(A):
    stack = []
    
    for e in A:
        stack.append(e)
        if len(stack) > 1:
            if stack[-1] != stack[-2]:
                stack.pop()
                stack.pop()
    
    if len(stack) > 0:    
        count = 0
        dominator = stack[0]
        for index in range(len(A)):
            if A[index] == dominator:
                count += 1
        if count > (len(A) //2):
            return A.index(dominator)
        return -1
    else:
        return -1