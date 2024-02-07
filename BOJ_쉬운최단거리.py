# BFS dist
from collections import deque

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

start = -1, -1
stones = []
for i in range(n):
    for j in range(m):
        if table[i][j] == 2:
            start = i, j
        if table[i][j] == 0:
            stones.append((i, j))

dist = [[-1 for _ in range(m)] for _ in range(n)]
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def valid(p):
    return 0<=p[0]<n and 0<=p[1]<m

dist[start[0]][start[1]] = 0
que = deque([start])
while que:
    now = que.popleft()
    for d in dxy:
        a = now[0]+d[0], now[1]+d[1]
        if valid(a) and table[a[0]][a[1]] == 1 and dist[a[0]][a[1]] == -1:
            dist[a[0]][a[1]] = dist[now[0]][now[1]] + 1
            que.append(a)

for i, j in stones:
    dist[i][j] = 0
for di in dist:
    print(*di)