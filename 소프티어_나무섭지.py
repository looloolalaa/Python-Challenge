# 유령보다 빨리 도착할 수 있는가
from collections import deque

n, m = map(int, input().split())
table = [input() for _ in range(n)]

now = -1, -1
door = -1, -1
ghosts = []
for i in range(n):
    for j in range(m):
        if table[i][j] == 'N':
            now = i, j
        if table[i][j] == 'D':
            door = i, j
        if table[i][j] == 'G':
            ghosts.append((i, j))

dxy = [[0,1], [1,0], [0,-1], [-1, 0]]
def valid(p):
    return 0<=p[0]<n and 0<=p[1]<m

dist = [[-1 for _ in range(m)] for _ in range(n)]
dist[now[0]][now[1]] = 0
que = deque([now])
while que:
    p = que.popleft()
    for d in dxy:
        a = p[0]+d[0], p[1]+d[1]
        if valid(a) and table[a[0]][a[1]] != '#' and dist[a[0]][a[1]] == -1:
            dist[a[0]][a[1]] = dist[p[0]][p[1]] + 1
            que.append(a)

my_dist = dist[door[0]][door[1]]
if my_dist == -1:
    print('No')
    exit(0)

ghosts_dist = [abs(g[0]-door[0])+abs(g[1]-door[1]) for g in ghosts]
if any(di<=my_dist for di in ghosts_dist):
    print('No')
else:
    print('Yes')
