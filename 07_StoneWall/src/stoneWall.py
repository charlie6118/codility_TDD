def solution(A):
    ## official solution
    N = len(A)
    stack = [0] * N
    stones = 0
    stack_num = 0

    for e in A:
        while stack_num > 0 and stack[stack_num - 1] > e:
            stack_num -= 1
        print(stack)
        if stack_num > 0 and stack[stack_num - 1] == e:
            pass
        else:
            stones += 1
            stack[stack_num] = e
            stack_num += 1
    return stones

print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))