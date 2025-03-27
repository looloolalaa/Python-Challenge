# 가장 가까운 병원 (벽이 없다면 que X)
from collections import deque

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


def total_dist():
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    que = deque()
    people = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                people.append((i, j))
            elif table[i][j] == 2:
                dist[i][j] = 0
                que.append((i, j))

    while que:
        now = que.popleft()
        for d in dxy:
            a = now[0] + d[0], now[1] + d[1]
            if valid(a) and dist[a[0]][a[1]] == -1:
                dist[a[0]][a[1]] = dist[now[0]][now[1]] + 1
                que.append(a)

    total = 0
    for person in people:
        total += dist[person[0]][person[1]]
    return total


hospitals = []
for i in range(n):
    for j in range(n):
        if table[i][j] == 2:
            hospitals.append((i, j))
            table[i][j] = 0


def on(sel):
    for p in sel:
        table[p[0]][p[1]] = 2


def off(sel):
    for p in sel:
        table[p[0]][p[1]] = 0


ans = int(1e9)
selected = []


def dfs(start):
    if len(selected) == m:
        global ans
        on(selected)
        ans = min(ans, total_dist())
        off(selected)
        return

    for j in range(start, len(hospitals)):
        selected.append(hospitals[j])
        dfs(j + 1)
        selected.pop()


dfs(0)
print(ans)