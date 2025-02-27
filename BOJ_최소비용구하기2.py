# 최단 경로(루트) 구하기 + 다익스트라
from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = defaultdict(dict)
for _ in range(m):
    a, b, c = map(int, input().split())
    if b not in graph[a]:
        graph[a][b] = c
    else:
        graph[a][b] = min(graph[a][b], c)


A, B = map(int, input().split())
dist = [float('inf') for _ in range(n+1)]
before = [-1 for _ in range(n+1)]

dist[A] = 0
h = [(0, A)]
while h:
    di, v = heapq.heappop(h)
    if di > dist[v]:
        continue

    for a in graph[v]:
        new_di = di + graph[v][a]
        if dist[a] > new_di:
            dist[a] = new_di
            heapq.heappush(h, (new_di, a))
            before[a] = v

ans = []
end = B
while end != -1:
    ans.append(end)
    end = before[end]
ans.reverse()

print(dist[B])
print(len(ans))
print(' '.join(map(str, ans)))
