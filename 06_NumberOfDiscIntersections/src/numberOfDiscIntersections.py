def solution(A):
    events = []
    for center, radius in enumerate(A):
        events += [(center-radius, +1), (center+radius, -1)]

    def getFirst(e):
        return e[0]
    events = sorted(events, key = getFirst)
    print(events)
    intersections, active_circles = 0, 0
    for _, circle_count_delta in events:
        print(active_circles, circle_count_delta, (circle_count_delta > 0))
        intersections += active_circles * (circle_count_delta > 0)
        active_circles += circle_count_delta
        if intersections > 10E6:
            return -1
    return intersections

print(solution([1, 5, 2, 1, 4, 0]))