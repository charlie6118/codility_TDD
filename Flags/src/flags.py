def solution(A):
    # write your code in Python 3.6
    lenA = len(A)
    peaks = [False] * lenA
    max_flag_num = 0
    for index in range(1, lenA - 1):
        if A[index - 1] < A[index] > A[index + 1]:
            peaks[index] = True
            max_flag_num += 1
    print(peaks)
    print(max_flag_num)

    for flag_num in reversed(range(1, max_flag_num + 1)):
        print(flag_num)
        pos = 0
        flag = flag_num
        while pos < lenA and flag > 0:
            if peaks[pos] == True:
                pos += flag_num
                flag -= 1
            else:
                pos += 1
        if flag == 0:
            return flag_num
    return 0

        
print(solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))