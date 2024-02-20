# BFS
from collections import deque

N, K = map(int, input().split())

dist = [-1 for _ in range(100_000+1)]

dist[N] = 0
que = deque([(N, 0)])
while que:
    x, d = que.popleft()
    if x != 0:
        k = 2*x
        while k <= 100_000:
            if dist[k] == -1:
                dist[k] = d
                que.append((k, d))
            k *= 2

    if 0 <= x-1 and dist[x - 1] == -1:
        dist[x-1] = d+1
        que.append((x - 1, d + 1))
    if x+1 <= 100_000 and dist[x + 1] == -1:
        dist[x+1] = d+1
        que.append((x + 1, d + 1))


print(dist[K])