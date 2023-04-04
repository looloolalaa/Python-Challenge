# look and say 알고리즘
# 개수 세기
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
attacks = [list(map(int, input().split())) for _ in range(m)]


def four(arr):
    result = []
    i = 0
    while i < len(arr):
        count = 1
        while i < len(arr) - 1 and arr[i] == arr[i + 1]:
            i += 1
            count += 1
        result.extend([count, arr[i]])
        i += 1
    return result


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


orders = []


def init_orders():
    temp_dxy = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    now = n // 2, n // 2
    count = 0
    d = 0

    while valid(now):
        if d % 2 == 0:
            count += 1
        for _ in range(count):
            orders.append(now)
            now = now[0] + temp_dxy[d][0], now[1] + temp_dxy[d][1]
            if not valid(now):
                break
        d = (d + 1) % 4


dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
score = 0


def one(arrow, dist):
    global score
    center = n // 2, n // 2
    for _ in range(dist):
        center = center[0] + dxy[arrow][0], center[1] + dxy[arrow][1]
        if board[center[0]][center[1]] > 0:
            score += board[center[0]][center[1]]
            board[center[0]][center[1]] = 0


def deleted(line):
    global score

    remain = []
    i = 0
    while i < len(line):
        count = 1
        while i < len(line) - 1 and line[i] == line[i + 1]:
            i += 1
            count += 1

        if count < 4:
            remain.append((count, line[i]))
        else:
            score += count * line[i]
        i += 1

    result = []
    for c, n in remain:
        for _ in range(c):
            result.append(n)
    return result


def two_and_three_and_four():
    line = []
    for i, j in orders:
        if board[i][j] > 0:
            line.append(board[i][j])
            board[i][j] = 0

    if not line:
        return

    next_line = deleted(line)
    while line != next_line:
        line = next_line
        next_line = deleted(line)

    new_line = four(line)
    new_line = new_line[:(n * n) - 1]
    for i in range(len(new_line)):
        p = orders[i + 1]
        board[p[0]][p[1]] = new_line[i]


init_orders()
for d, p in attacks:
    one(d, p)
    two_and_three_and_four()
print(score)

