# 다익스트라 변형: 출발 지점 여러개
from collections import defaultdict
import heapq


def solution(n, paths, gates, summits):
    gates, summits = set(gates), set(summits)
    graph = defaultdict(dict)
    for a, b, c in paths:
        graph[a][b] = c
        graph[b][a] = c
        if (a in summits or b in gates) and b in graph[a]:
            graph[a].pop(b)
        if (a in gates or b in summits) and a in graph[b]:
            graph[b].pop(a)

    # print(graph)

    dis = [float('inf') for _ in range(n + 1)]
    h = []
    for g in gates:
        dis[g] = 0
        h.append((0, g))

    while h:
        d, i = heapq.heappop(h)
        if d > dis[i]:
            continue

        for a in graph[i]:
            new_d = max(dis[i], graph[i][a])
            if new_d < dis[a]:
                dis[a] = new_d
                heapq.heappush(h, (new_d, a))

    result = [float('inf'), float('inf')]
    for s in summits:
        value = dis[s]
        if value < result[1]:
            result = [s, dis[s]]
        elif value == result[1] and s < result[0]:
            result[0] = s
    return result