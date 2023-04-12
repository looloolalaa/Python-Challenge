# MST - Prim 알고리즘
from collections import defaultdict
import heapq


def solution(n, costs):
    graph = defaultdict(dict)
    for a, b, c in costs:
        graph[a][b] = c
        graph[b][a] = c

    dis = [float('inf') for _ in range(n)]
    h = [(0, 0)]
    while h:
        d, n = heapq.heappop(h)
        if dis[n] != float('inf'):
            continue

        dis[n] = d
        for a in graph[n]:
            heapq.heappush(h, (graph[n][a], a))

    # print(dis)
    return sum(dis)