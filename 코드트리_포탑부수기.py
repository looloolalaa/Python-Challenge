# 2023 상반기 삼성 코테 오전 1번
from collections import deque

n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
time = [[0 for _ in range(m)] for _ in range(n)]

def time_up():
    for i in range(n):
        for j in range(m):
            if table[i][j] > 0:
                time[i][j] += 1

def plus(p, d):
    nx = p[0]+d[0]
    if nx < 0:
        nx = n-1
    elif nx >= n:
        nx = 0

    ny = p[1]+d[1]
    if ny < 0:
        ny = m - 1
    elif ny >= m:
        ny = 0

    return nx, ny

def get_bundle(r, c):
    return table[r][c], time[r][c], -(r+c), -c

def get_power():
    me = -1, -1
    min_bundle = float('inf'), float('inf'), float('inf'), float('inf')
    for r in range(n):
        for c in range(m):
            if table[r][c] > 0:
                bundle = get_bundle(r, c)
                if bundle < min_bundle:
                    me = (r, c)
                    min_bundle = bundle

    table[me[0]][me[1]] += n + m
    time[me[0]][me[1]] = 0
    return me

def get_target(me):
    you = -1, -1
    max_bundle = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if table[i][j] == 0 or (i, j) == me:
                continue

            bundle = get_bundle(i, j)
            if bundle > max_bundle:
                you = (i, j)
                max_bundle = bundle
    return you


dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
arrows = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
dis = [[-1 for _ in range(m)] for _ in range(n)]
def attack(me, you):
    impact = [me, you]

    for i in range(n):
        for j in range(m):
            dis[i][j] = -1

    dis[you[0]][you[1]] = 0
    q = deque([you])
    while q:
        now = q.popleft()
        for d in dxy:
            a = plus(now, d)
            if table[a[0]][a[1]] > 0 and dis[a[0]][a[1]] == -1:
                dis[a[0]][a[1]] = dis[now[0]][now[1]] + 1
                q.append(a)


    p = table[me[0]][me[1]]
    if dis[me[0]][me[1]] != -1:
        start = me
        route = []
        while True:
            # move
            arrow = 0, 0
            min_d = float('inf')
            for d in dxy:
                a = plus(start, d)
                if table[a[0]][a[1]] > 0 and min_d > dis[a[0]][a[1]]:
                    min_d = dis[a[0]][a[1]]
                    arrow = d

            start = plus(start, arrow)
            if start == you:
                break
            route.append(start)

        table[you[0]][you[1]] -= p
        for r, c in route:
            table[r][c] -= int(p/2)

        impact.extend(route)

        for i in range(n):
            for j in range(m):
                if table[i][j] <= 0:
                    table[i][j] = 0

    else:
        table[you[0]][you[1]] -= p
        for d in arrows:
            a = plus(you, d)
            if table[a[0]][a[1]] > 0 and a != me:
                table[a[0]][a[1]] -= int(p/2)
                impact.append(a)

        for i in range(n):
            for j in range(m):
                if table[i][j] <= 0:
                    table[i][j] = 0

    return impact


def grow(impact):
    temp = [[False for _ in range(m)] for _ in range(n)]
    for r, c in impact:
        temp[r][c] = True

    for i in range(n):
        for j in range(m):
            if table[i][j] > 0 and not temp[i][j]:
                table[i][j] += 1

def simulate():
    time_up()
    me = get_power()
    you = get_target(me)
    impact = attack(me, you)
    grow(impact)

def god_count():
    count = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] > 0:
                count += 1
    return count


# for t in table:
#     print(t)
for _ in range(k):
    if god_count() == 1:
        break

    simulate()

result = 0
for i in range(n):
    for j in range(m):
        result = max(result, table[i][j])

print(result)
