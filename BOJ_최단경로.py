# 경로 여러개 그래프 dijkstra(다익스트라)
from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)
dist = [float('inf') for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(s):
    dist[s] = 0
    h = [(0, s)]

    while h:
        d, v = heapq.heappop(h)
        if dist[v] < d:
            continue

        for a, ad in graph[v]:
            new_dist = d + ad
            if dist[a] > new_dist:
                dist[a] = new_dist
                heapq.heappush(h, (new_dist, a))

dijkstra(K)
for i in range(1, V+1):
    print('INF' if dist[i] == float('inf') else dist[i])
