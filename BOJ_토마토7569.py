# 3차원 BFS
from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

que = deque()
next_que = deque()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                que.append((h, n, m))


dxyz = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]
def valid(p):
    return 0 <= p[0] < H and 0 <= p[1] < N and 0 <= p[2] < M

def bfs():
    while que:
        now = que.popleft()
        for d in dxyz:
            a = now[0]+d[0], now[1]+d[1], now[2]+d[2]
            if valid(a) and box[a[0]][a[1]][a[2]] == 0:
                box[a[0]][a[1]][a[2]] = 1
                next_que.append(a)


day = 0
while que:
    bfs()
    que = next_que.copy()
    next_que.clear()
    day += 1

for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                print(-1)
                exit(0)

print(day-1)