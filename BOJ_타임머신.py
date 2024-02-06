# 벨만-포드
from collections import defaultdict

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

INF = int(1e9)
dist = [INF for _ in range(N+1)]

dist[1] = 0
for i in range(N-1):
    for s in graph:
        for e, t in graph[s]:
            if dist[s] != INF and dist[e] > dist[s] + t:
                dist[e] = dist[s] + t

for s in graph:
    for e, t in graph[s]:
        if dist[s] != INF and dist[e] > dist[s] + t:
            print(-1)
            exit(0)

for e in range(2, N+1):
    print(dist[e] if dist[e] != INF else -1)