# MST - 프림(Prim)
from collections import defaultdict
import heapq


def solution(n, costs):
    graph = defaultdict(list)
    for a, b, c in costs:
        graph[a].append((b, c))
        graph[b].append((a, c))

    dist = [float('inf') for _ in range(n)]

    h = [(0, 0)]
    while h:
        d, v = heapq.heappop(h)
        if dist[v] < d:
            continue

        dist[v] = d
        for a, ad in graph[v]:
            if dist[a] == float('inf'):
                heapq.heappush(h, (ad, a))

    return sum(dist)