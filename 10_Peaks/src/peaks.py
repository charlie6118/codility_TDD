def solution(N):
    peaksIndex = []
 
    for idx in range(1, len(N)-1):
        if N[idx-1] < N[idx] > N[idx+1]:
            peaksIndex.append(idx)

    if len(peaksIndex) == 0:
        return 0

    totalN = len(N) #12

    for i in reversed(range(1, len(peaksIndex) + 1)):
        if totalN % i == 0:
            K = (totalN // i)
            found = [False] * totalN
            found_cnt = 0
            for peak in peaksIndex:
                block_nr = peak // K
                print(block_nr)
                if found[block_nr] == False:
                    found[block_nr] = True
                    found_cnt += 1
            if found_cnt == i:
                return i
    return 0

solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2])
