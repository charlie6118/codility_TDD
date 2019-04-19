def fab(n):
    F = [0] * 27
    F[1] = 1
    for i in range(2, 27):
        F[i] = F[i - 1] + F[i - 2]
        if F[i] > n:
            return F[2: i]
        else:
            last_valid = i
        
def solution(A):
    A.append(1)

    fSteps = fab(len(A))
    reachable = [-1] * len(A)

    for step in fSteps:
        if A[step - 1] > 0:
            reachable[step - 1] = 1

    for idx, leaf in enumerate(A):
        if leaf == 0 or reachable[idx] > 0:
            continue
        min_idx = -1
        min_step = 10000
        for step in fSteps:
            pre_idx = idx - step
            if pre_idx < 0:
                break
            if reachable[pre_idx] > 0 and min_step > reachable[pre_idx]:
                min_idx = pre_idx
                min_step = reachable[pre_idx]
        if min_idx != -1:
            reachable[idx] = min_step + 1
    return reachable[len(A) - 1]