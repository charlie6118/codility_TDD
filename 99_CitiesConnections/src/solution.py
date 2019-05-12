# O(M)
def findCapital(A):
        for idx, city in enumerate(A):
            if idx == city:
                return idx

# O(M), create graph of cities
def citiesConnections(A):
    capital = findCapital(A)
    dic = {}
    for idx, city in enumerate(A):
        if idx == capital: continue
        if city not in dic.keys():
            dic[city] = [idx]
        else:
            dic[city].append(idx)
    return dic

# O(M), mark depth of each node
def markLayers(graph, source, acc, layer):
    acc[source] = layer
    if source in graph.keys():
        for city in graph[source]:
            markLayers(graph, city, acc, layer + 1)
    return acc

def solution(A):
    if not A or len(A) == 1: return []
    capital = findCapital(A)
    cityMap = citiesConnections(A)
    cityDepth = markLayers(cityMap, capital, A, 0)
    res = [0] * (len(A))
    # O(M), count depth of each nodes
    for c in cityDepth:
        res[c] += 1
    return res[1:]
    