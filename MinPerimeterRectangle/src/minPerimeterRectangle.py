def solution(N):
    i = 1
    pairs = []
    while (i * i < N):
        if (N % i == 0):
            pairs.append((i, N//i))
        i += 1
    if i * i == N:
        pairs.append((i, i))
    minPerimeter = (1 + N) * 2
    for (A, B) in pairs:
        minPerimeter = min(minPerimeter, 2 * (A + B))
    return(minPerimeter)

solution(30)