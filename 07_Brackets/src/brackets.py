def solution(S):
    left = '[{('
    right = ']})'
    neutral = 'UuVvOoAIiHlMTXx'
    stack = []
    for char in S:
        if char in left:
            stack.append(char)
        if char in right:
            if len(stack) == 0:
                return 0
            elif stack[-1] == left[right.index(char)]:
                stack.pop()
            else:
                stack.append(char)
        if char in neutral:
            pass
    if len(stack) == 0:
        return 1
    return 0