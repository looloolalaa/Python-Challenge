# 그래프의 지름: 완탐
from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
dist = [[-1 for _ in range(M)] for _ in range(N)]

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def valid(p):
    return 0 <= p[0] < N and 0 <= p[1] < M


def bfs(p):
    visited = [p]
    que = deque([p])
    dist[p[0]][p[1]] = 0
    while que:
        now = que.popleft()
        for d in dxy:
            a = now[0]+d[0], now[1]+d[1]
            if valid(a) and arr[a[0]][a[1]] == 'L' and dist[a[0]][a[1]] == -1:
                dist[a[0]][a[1]] = dist[now[0]][now[1]] + 1
                que.append(a)
                visited.append(a)

    maxi = max(dist[v[0]][v[1]] for v in visited)
    for v in visited:
        dist[v[0]][v[1]] = -1
    return maxi


ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            ans = max(ans, bfs((i, j)))

print(ans)