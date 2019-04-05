def solution(A, B):
    downstream = 0
    upstream = []

    for i in range(len(A)):
        if B[i] == 0:
            while len(upstream) != 0:
                if upstream[-1] > A[i]:
                    break
                else:
                    upstream.pop()
            else:
                downstream += 1
        else:
            upstream.append(A[i])
    
    return (downstream + len(upstream))

solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0])
# solution([1], [0])