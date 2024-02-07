# BFS 최대거리
from collections import deque

M, N = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]


que = deque()
for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            que.append((i, j))

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def valid(p):
    return 0<=p[0]<N and 0<=p[1]<M

while que:
    now = que.popleft()
    for d in dxy:
        a = now[0]+d[0], now[1]+d[1]
        if valid(a) and table[a[0]][a[1]] == 0:
            table[a[0]][a[1]] = table[now[0]][now[1]] + 1
            que.append(a)

maxi = 0
for i in range(N):
    for j in range(M):
        if table[i][j] == 0:
            print(-1)
            exit()
        maxi = max(maxi, table[i][j])

print(maxi-1)