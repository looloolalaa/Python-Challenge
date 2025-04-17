# dfs 연결개수가 3개 이상
K, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(5)]
wall = list(map(int, input().split()))


def rotate(p):
    origin = [
        [(p[0] - 1, p[1] - 1), (p[0] - 1, p[1]), (p[0] - 1, p[1] + 1)],
        [(p[0], p[1] - 1), (p[0], p[1]), (p[0], p[1] + 1)],
        [(p[0] + 1, p[1] - 1), (p[0] + 1, p[1]), (p[0] + 1, p[1] + 1)],
    ]
    origin = [[board[b[0]][b[1]] for b in a] for a in origin]

    rotated = list(zip(*origin[::-1]))
    for i in range(3):
        for j in range(3):
            board[i + p[0] - 1][j + p[1] - 1] = rotated[i][j]


dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def valid(p):
    return 0 <= p[0] < 5 and 0 <= p[1] < 5


def will_dead():
    visited = [[False for _ in range(5)] for _ in range(5)]

    connected = []

    def dfs(p, num):
        for d in dxy:
            a = p[0] + d[0], p[1] + d[1]
            if valid(a) and not visited[a[0]][a[1]] and board[a[0]][a[1]] == num:
                connected.append(a)
                visited[a[0]][a[1]] = True
                dfs(a, num)

    dead = []
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                connected = [(i, j)]
                visited[i][j] = True
                dfs((i, j), board[i][j])
                if len(connected) >= 3:
                    dead += connected

    return dead


pointer = 0


def fill():
    global pointer
    for j in range(5):
        for i in range(4, -1, -1):
            if board[i][j] == 0:
                board[i][j] = wall[pointer]
                pointer += 1


for _ in range(K):
    candi = []
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(3):
                rotate((i, j))
                candi.append((will_dead(), k + 1, (i, j)))
            rotate((i, j))

    target = min(candi, key=lambda x: (-len(x[0]), x[1], (x[2][1], x[2][0])))
    if not target[0]:
        break

    for _ in range(target[1]):
        rotate(target[2])

    value = len(target[0])
    for p in target[0]:
        board[p[0]][p[1]] = 0
    fill()

    # 연쇄
    while True:
        dead = will_dead()
        value += len(dead)
        if not dead:
            break

        for d in dead:
            board[d[0]][d[1]] = 0
        fill()

    print(value, end=' ')


