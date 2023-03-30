# 벽 + 바람 불기 + 차이 분배
# 벽: p 에서 4방향으로 있는가로 정의
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
wall = [[[False, False] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, s = map(int, input().split())
    wall[x - 1][y - 1][s] = True

room = [[0 for _ in range(n)] for _ in range(n)]
dxy = {2: [0, -1], 3: [-1, 0], 4: [0, 1], 5: [1, 0]}


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


plused = [[0 for _ in range(n)] for _ in range(n)]


def turn_on(p):
    temp_room = [[0 for _ in range(n)] for _ in range(n)]
    d = board[p[0]][p[1]]  # 4
    arrow = dxy[d]
    start = p[0] + arrow[0], p[1] + arrow[1]

    up, down = arrow, arrow
    if arrow[0] == 0:
        up, down = [-1, arrow[1]], [1, arrow[1]]
    elif arrow[1] == 0:
        up, down = [arrow[0], -1], [arrow[0], 1]
    arrows = [up, arrow, down]

    def dfs(p, wind):
        def can_go(arrow):
            next_p = p[0] + arrow[0], p[1] + arrow[1]
            if not valid(next_p):
                return False

            if arrow[0] == 0 or arrow[1] == 0:
                if arrow == [0, 1]:
                    return wall[next_p[0]][next_p[1]][1] == False
                elif arrow == [1, 0]:
                    return wall[next_p[0]][next_p[1]][0] == False
                elif arrow == [0, -1]:
                    return wall[p[0]][p[1]][1] == False
                elif arrow == [-1, 0]:
                    return wall[p[0]][p[1]][0] == False

            # right
            if d == 4:
                if arrow == [-1, 1]:
                    return wall[p[0]][p[1]][0] == False and wall[next_p[0]][next_p[1]][1] == False
                elif arrow == [1, 1]:
                    bottom = (p[0] + 1, p[1])
                    return wall[bottom[0]][bottom[1]][0] == False and wall[next_p[0]][next_p[1]][1] == False
            # up
            elif d == 3:
                if arrow == [-1, -1]:
                    left = (p[0], p[1] - 1)
                    return wall[p[0]][p[1]][1] == False and wall[left[0]][left[1]][0] == False
                elif arrow == [-1, 1]:
                    right = (p[0], p[1] + 1)
                    return wall[right[0]][right[1]][1] == False and wall[right[0]][right[1]][0] == False
            # left
            elif d == 2:
                if arrow == [-1, -1]:
                    up = (p[0] - 1, p[1])
                    return wall[p[0]][p[1]][0] == False and wall[up[0]][up[1]][1] == False
                elif arrow == [1, -1]:
                    down = (p[0] + 1, p[1])
                    return wall[down[0]][down[1]][0] == False and wall[down[0]][down[1]][1] == False
            # down
            elif d == 5:
                if arrow == [1, -1]:
                    return wall[p[0]][p[1]][1] == False and wall[next_p[0]][next_p[1]][0] == False
                elif arrow == [1, 1]:
                    right = (p[0], p[1] + 1)
                    return wall[right[0]][right[1]][1] == False and wall[next_p[0]][next_p[1]][0] == False

            return True

        if wind == 0:
            return

        temp_room[p[0]][p[1]] = wind
        for arro in arrows:
            if can_go(arro):
                next_p = p[0] + arro[0], p[1] + arro[1]
                dfs(next_p, wind - 1)

    dfs(start, 5)
    for i in range(n):
        for j in range(n):
            plused[i][j] += temp_room[i][j]


def cool():
    for i in range(n):
        for j in range(n):
            if 2 <= board[i][j] <= 5:
                # if board[i][j] == 3:
                turn_on((i, j))


def mix():
    temp_dxy = [[0, 1], [1, 0]]
    diff = {}
    for i in range(n):
        for j in range(n):
            for k in range(2):
                d = temp_dxy[k]
                a = i + d[0], j + d[1]
                if valid(a):
                    if k == 0:
                        if wall[a[0]][a[1]][1] == True:
                            continue
                    elif k == 1:
                        if wall[a[0]][a[1]][0] == True:
                            continue

                    small, big = ((i, j), a) if room[i][j] < room[a[0]][a[1]] else (a, (i, j))
                    diff[(big, small)] = abs(room[i][j] - room[a[0]][a[1]])

    for key in diff:
        big, small = key
        room[big[0]][big[1]] -= int(diff[key] / 4)
        room[small[0]][small[1]] += int(diff[key] / 4)


def decrease():
    for j in range(n):
        if room[0][j] > 0:
            room[0][j] -= 1
    for j in range(n):
        if room[n - 1][j] > 0:
            room[n - 1][j] -= 1

    for i in range(1, n - 1):
        if room[i][0] > 0:
            room[i][0] -= 1
        if room[i][n - 1] > 0:
            room[i][n - 1] -= 1


def plus():
    for i in range(n):
        for j in range(n):
            room[i][j] += plused[i][j]


def simulate():
    plus()
    mix()
    decrease()


offices = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            offices.append((i, j))


def all_cool():
    return all(room[office[0]][office[1]] >= k for office in offices)


cool()
time = 0
while not all_cool():
    simulate()
    time += 1
    if time > 100:
        print(-1)
        exit()

print(time)