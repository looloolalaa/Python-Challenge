# 시뮬레이션
n, m, k, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == -1:
            board[i][j] = -float('inf')


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

trees = {}


def grow_up():
    trees.clear()
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                count = 0
                for d in dxy:
                    a = i + d[0], j + d[1]
                    if valid(a) and board[a[0]][a[1]] > 0:
                        count += 1
                trees[(i, j)] = count

    for p in trees:
        board[p[0]][p[1]] += trees[p]


def spread():
    for p in trees:
        count = 0
        for d in dxy:
            a = p[0] + d[0], p[1] + d[1]
            if valid(a) and board[a[0]][a[1]] == 0:
                count += 1

        trees[p] = count

    for p in trees:
        if trees[p] == 0:
            continue

        child = board[p[0]][p[1]] // trees[p]
        for d in dxy:
            a = p[0] + d[0], p[1] + d[1]
            if valid(a) and board[a[0]][a[1]] >= 0 and a not in trees:
                board[a[0]][a[1]] += child


diago = [[-1, 1], [1, 1], [1, -1], [-1, -1]]


def around(p):
    now = p
    around = []
    for d in diago:
        a = now[0] + d[0], now[1] + d[1]
        c = k
        while valid(a) and board[a[0]][a[1]] != -float('inf') and c > 0:
            around.append(a)
            c -= 1
            if board[a[0]][a[1]] == 0 or board[a[0]][a[1]] < 0:
                break
            a = a[0] + d[0], a[1] + d[1]

    return around


def dead_count(p):
    return board[p[0]][p[1]] + sum(board[a[0]][a[1]] for a in around(p) if board[a[0]][a[1]] > 0)


result = 0


def kill():
    global result
    target = -1, -1
    max_dead = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                dead = dead_count((i, j))
                if dead > max_dead:
                    target = i, j
                    max_dead = dead_count((i, j))

    result += max_dead
    board[target[0]][target[1]] = -c - 1
    for a in around(target):
        board[a[0]][a[1]] = -c - 1


def plus():
    for i in range(n):
        for j in range(n):
            if board[i][j] < 0:
                board[i][j] += 1


def simulate():
    plus()
    grow_up()
    spread()
    kill()


for _ in range(m):
    simulate()

print(result)
# for b in board:
#     print(b)