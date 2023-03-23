# BFS(목적지)
# 목적지까지 최단거리로 가는 다음 방향?
# ==> BFS를 목적지에서 출발시켜 최단 거리 구한 후
# 시작점 주위 4방향으로 최단 거리 탐색하여 방향 찾기
# next_step2
from collections import deque


pos = {}
des = {}
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, m + 1):
    a, b = map(int, input().split())
    des[i] = (a - 1, b - 1)

dxy = [[-1, 0], [0, -1], [0, 1], [1, 0]]


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n



def next_step2(k):
    dis = [[-1 for _ in range(n)] for _ in range(n)]
    start = des[k]
    q = deque()
    q.append(start)
    dis[start[0]][start[1]] = 0
    while q:
        now = q.popleft()
        for d in dxy:
            a = now[0] + d[0], now[1] + d[1]
            if valid(a) and dis[a[0]][a[1]] == -1:
                dis[a[0]][a[1]] = dis[now[0]][now[1]] + 1
                q.append(a)

    min_arrow = -1, -1
    min_dis = float('inf')
    p = pos[k]
    for i in range(4):
        d = dxy[i]
        a = p[0] + d[0], p[1] + d[1]
        if valid(a) and dis[a[0]][a[1]] != -1 and min_dis > dis[a[0]][a[1]]:
            min_dis = dis[a[0]][a[1]]
            min_arrow = i

    return min_arrow


def next_step(k):
    routes = [[[] for _ in range(n)] for _ in range(n)]
    start = pos[k]

    q = deque([start])
    routes[start[0]][start[1]] = [-1]
    while q:
        now = q.popleft()
        if now == des[k]:
            return routes[des[k][0]][des[k][1]][1]

        for i in range(4):
            d = dxy[i]
            a = now[0] + d[0], now[1] + d[1]
            if valid(a) and table[a[0]][a[1]] != 2:
                new_route = routes[now[0]][now[1]] + [i]
                if routes[a[0]][a[1]] == [] or len(new_route) < len(routes[a[0]][a[1]]):
                    routes[a[0]][a[1]] = new_route
                    q.append(a)
                elif len(new_route) == len(routes[a[0]][a[1]]):
                    routes[a[0]][a[1]] = min(new_route, routes[a[0]][a[1]])
                    q.append(a)

    steps = routes[des[k][0]][des[k][1]]
    return steps[1] if len(steps) > 1 else -1


def shortest_camp(k):
    dis = [[-1 for _ in range(n)] for _ in range(n)]
    start = des[k]
    dis[start[0]][start[1]] = 0

    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for d in dxy:
            a = now[0] + d[0], now[1] + d[1]
            if valid(a) and table[a[0]][a[1]] != 2 and dis[a[0]][a[1]] == -1:
                dis[a[0]][a[1]] = dis[now[0]][now[1]] + 1
                q.append(a)

    candis = []
    for i in range(n):
        for j in range(n):
            # asdasdasdasd
            if table[i][j] == 1 and dis[i][j] != -1:
                candis.append((dis[i][j], i, j))
    candis.sort()

    return candis[0][1], candis[0][2]


def go():
    for r in remain:
        if r in pos:
            step = next_step(r)
            d = dxy[step]
            p = pos[r]
            pos[r] = p[0] + d[0], p[1] + d[1]


def check():
    arrived = []
    for person in pos:
        if pos[person] == des[person]:
            arrived.append(person)

    for person in arrived:
        p = pos[person]
        table[p[0]][p[1]] = 2
        pos.pop(person)
        remain.remove(person)


def get_in():
    if time <= m:
        person = time
        camp = shortest_camp(person)
        pos[person] = camp
        table[camp[0]][camp[1]] = 2


time = 0
remain = set(i for i in range(1, m + 1))
while remain:
    # print(time, pos)
    time += 1
    go()
    check()
    get_in()

print(time)
