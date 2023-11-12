# 다익스트라(dijkstra) 응용 (반대 방향)
import heapq
from collections import defaultdict

N, M, X = map(int, input().split())
graph1 = defaultdict(dict)
graph2 = defaultdict(dict)
dist1 = [float('inf') for _ in range(N+1)]
dist2 = [float('inf') for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph1[s][e] = t
    graph2[e][s] = t

def dijkstra(s):
    dist = dist1 if isFirst else dist2
    graph = graph1 if isFirst else graph2

    dist[s] = 0
    h = [(0, s)]
    while h:
        d, v = heapq.heappop(h)
        if dist[v] < d:
            continue

        for a in graph[v]:
            new_dist = d + graph[v][a]
            if dist[a] > new_dist:
                dist[a] = new_dist
                heapq.heappush(h, (new_dist, a))

isFirst = True
dijkstra(X)
isFirst = not isFirst
dijkstra(X)


print(max(dist1[i] + dist2[i] for i in range(1, N+1)))

