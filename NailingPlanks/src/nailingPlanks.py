def solution(A, B, C):
    C = sorted(C)
    nailed_planks = [-1] * len(A)
    used_nails = 0
    planks_num = len(A)
    planks_idx = 0
    pre_nail = -1

    for nail in C:
        if A[planks_idx] == pre_nail or A[planks_idx] <= nail <= B[planks_idx]:
            if nailed_planks[planks_idx] < 0:
                used_nails += 1
                nailed_planks[planks_idx] = used_nails
            planks_idx += 1
        if planks_idx == planks_num:
            print(nailed_planks)
            return nailed_planks[-1]
        pre_nail = nail
    return nailed_planks[-1]