# 테두리만 큐에 넣기
from collections import deque

R, C = map(int, input().split())
table = [list(input()) for _ in range(R)]
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def valid(p):
    return 0 <= p[0] < R and 0 <= p[1] < C

water = deque()
ll = []
for i in range(R):
    for j in range(C):
        if table[i][j] == '.':
            water.append((i, j))
        elif table[i][j] == 'L':
            ll.append((i, j))

first, second = ll
table[first[0]][first[1]] = '.'
water.append(first)

swan = deque([second])


next_water = deque()
next_swan = deque()

water_visited = [[False]*C for _ in range(R)]
swan_visited = [[False]*C for _ in range(R)]

day = 0
while True:

    while swan:
        now = swan.popleft()
        if now == first:
            # for t in table:
            #     print(t)
            print(day)
            exit()

        swan_visited[now[0]][now[1]] = True
        for d in dxy:
            a = now[0] + d[0], now[1] + d[1]
            if valid(a) and not swan_visited[a[0]][a[1]]:
                swan_visited[a[0]][a[1]] = True
                if table[a[0]][a[1]] == 'X':
                    next_swan.append(a)
                elif table[a[0]][a[1]] == '.':
                    swan.append(a)

    # visited = set()
    while water:
        now = water.popleft()

        water_visited[now[0]][now[1]] = True
        for d in dxy:
            a = now[0] + d[0], now[1] + d[1]
            if valid(a) and not water_visited[a[0]][a[1]]:
                water_visited[a[0]][a[1]] = True
                if table[a[0]][a[1]] == 'X':
                    next_water.append(a)

                # elif table[a[0]][a[1]] == '.':
                #     water.append(a)

    for x, y in next_swan:
        table[x][y] = '.'
    for x, y in next_water:
        table[x][y] = '.'

    swan = next_swan
    next_swan = deque()
    water = next_water
    next_water = deque()

    day += 1




