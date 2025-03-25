# (d, i, j) 우선순위
from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
robot = -1, -1
level = 2
exp = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            robot = i, j
            grid[i][j] = 0

dxy = [[0,1], [1,0], [0,-1], [-1,0]]
def valid(p):
    return 0<=p[0]<n and 0<=p[1]<n


INF = int(1e9)
def target():
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    dist[robot[0]][robot[1]] = 0
    que = deque([robot])
    while que:
        now = que.popleft()
        for d in dxy:
            a = now[0]+d[0], now[1]+d[1]
            if valid(a) and dist[a[0]][a[1]] == -1 and grid[a[0]][a[1]] <= level:
                dist[a[0]][a[1]] = dist[now[0]][now[1]] + 1
                que.append(a)

    res = INF, INF, INF
    for i in range(n):
        for j in range(n):
            if 1 <= grid[i][j] < level and dist[i][j] != -1:
                res = min(res, (dist[i][j], i, j))
    return res

time = 0
while True:
    t = target()
    if t[0] == INF:
        break

    time += t[0]
    robot = t[1], t[2]
    grid[t[1]][t[2]] = 0
    exp += 1
    if exp == level:
        level += 1
        exp = 0

print(time)

# 00500
# 06170
# 820310
# 094110
# 001200
