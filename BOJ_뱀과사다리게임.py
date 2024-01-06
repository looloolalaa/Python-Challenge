# 주사위 BFS
from collections import deque

N, M = map(int, input().split())
teleports = {}
for _ in range(N+M):
    a, b = map(int, input().split())
    teleports[a] = b


dist = [-1 for _ in range(101)]
dist[1] = 0
que = deque([1])
while que:
    now = que.popleft()
    for i in range(1, 7):
        aim = now + i
        if aim <= 100 and dist[aim] == -1:
            dist[aim] = dist[now] + 1
            if aim in teleports:
                aim_next = teleports[aim]
                if dist[aim_next] == -1:
                    dist[aim_next] = dist[aim]
                    que.append(aim_next)
            else:
                que.append(aim)


print(dist[100])