# BFS - 현재 상태 저장
from collections import deque

N, M = map(int, input().split())
table = [input() for _ in range(N)]

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def valid(p):
    return 0 <= p[0] < N and 0 <= p[1] < M


dist = [[[float('inf'), float('inf')] for _ in range(M)] for _ in range(N)]
dist[0][0][0] = 0
que = deque([(0, 0, 0, False)])
while que:
    i, j, di, wall = que.popleft()
    for d in dxy:
        a = i+d[0], j+d[1]
        if valid(a):
            if wall:
                if table[a[0]][a[1]] == '0' and dist[a[0]][a[1]][1] == float('inf'):
                    dist[a[0]][a[1]][1] = di + 1
                    que.append((a[0], a[1], di+1, True))
            else:
                if table[a[0]][a[1]] == '0' and dist[a[0]][a[1]][0] == float('inf'):
                    dist[a[0]][a[1]][0] = di + 1
                    que.append((a[0], a[1], di+1, False))
                elif table[a[0]][a[1]] == '1' and dist[a[0]][a[1]][1] == float('inf'):
                    dist[a[0]][a[1]][1] = di + 1
                    que.append((a[0], a[1], di+1, True))


res = min(dist[-1][-1])
print(-1 if res == float('inf') else res + 1)
