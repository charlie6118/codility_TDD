def solution(A):
  
    maxA = max(A)
    count = {} # count the num of each element
    divisors = {} # decouple the divisors
    for e in A:
        if not count.get(e):
            count[e] = 1
        else:
            count[e] += 1
        divisors[e] = set([1, e])
    
    d = 2
    while d * d <= maxA:
        e_candidate = d
        while e_candidate <= maxA:
            if e_candidate in divisors and not d in divisors[e_candidate]:
                divisors[e_candidate].add(d)
                divisors[e_candidate].add(e_candidate // d)
            e_candidate += d
        d += 1

    result = [0] * len(A)
    for index, value in enumerate(A):
        temp_sum = 0
        for d in divisors[value]:
            # if count has no d, return zero
            temp_sum += count.get(d, 0)
        result[index] = len(A) - temp_sum
        
    return result