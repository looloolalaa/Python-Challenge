# dp가 아닌, 최소 횟수 BFS 탐색
from collections import deque

N, K = map(int, input().split())
que = deque([(N, 0)])
visited = set()

while que:
    n, count = que.popleft()
    if n < 0 or n > 100_000:
        continue

    if n == K:
        print(count)
        exit()
    if n in visited:
        continue

    visited.add(n)
    que.append((n-1, count+1))
    que.append((n+1, count + 1))
    que.append((2*n, count + 1))

