# 가로세로 테트리스
k = int(input())
blocks = [list(map(int, input().split())) for _ in range(k)]

board = [[0 for _ in range(10)] for _ in range(10)]


def put(block):
    t, x, y = block
    if t == 1:
        i = 4
        while i < 10 and board[i][y] == 0:
            i += 1
        board[i - 1][y] = 1

        j = 4
        while j < 10 and board[x][j] == 0:
            j += 1
        board[x][j - 1] = 1

    elif t == 2:
        i = 4
        while i < 10 and board[i][y] == 0 and board[i][y + 1] == 0:
            i += 1
        board[i - 1][y] = 1
        board[i - 1][y + 1] = 1

        j = 4
        while j < 10 and board[x][j] == 0:
            j += 1
        board[x][j - 1] = 1
        board[x][j - 2] = 1

    elif t == 3:
        i = 4
        while i < 10 and board[i][y] == 0:
            i += 1
        board[i - 1][y] = 1
        board[i - 2][y] = 1

        j = 4
        while j < 10 and board[x][j] == 0 and board[x + 1][j] == 0:
            j += 1
        board[x][j - 1] = 1
        board[x + 1][j - 1] = 1


score = 0


def erase():
    global score
    for i in range(6, 10):
        if board[i][0] == 1 and board[i][1] == 1 and board[i][2] == 1 and board[i][3] == 1:
            board[i][0] = 0
            board[i][1] = 0
            board[i][2] = 0
            board[i][3] = 0
            score += 1
    for j in range(6, 10):
        if board[0][j] == 1 and board[1][j] == 1 and board[2][j] == 1 and board[3][j] == 1:
            board[0][j] = 0
            board[1][j] = 0
            board[2][j] = 0
            board[3][j] = 0
            score += 1


def down():
    lines = []
    for j in range(4, 10):
        if board[0][j] == 1 or board[1][j] == 1 or board[2][j] == 1 or board[3][j] == 1:
            lines.append([board[0][j], board[1][j], board[2][j], board[3][j]])
            board[0][j] = 0
            board[1][j] = 0
            board[2][j] = 0
            board[3][j] = 0

    lines.reverse()
    k = 0
    for j in range(9, 9 - len(lines), -1):
        for i in range(4):
            board[i][j] = lines[k][i]
        k += 1

    lines2 = []
    for i in range(4, 10):
        if board[i][0] == 1 or board[i][1] == 1 or board[i][2] == 1 or board[i][3] == 1:
            lines2.append([board[i][0], board[i][1], board[i][2], board[i][3]])
            board[i][0] = 0
            board[i][1] = 0
            board[i][2] = 0
            board[i][3] = 0

    lines2.reverse()
    k = 0
    for i in range(9, 9 - len(lines2), -1):
        for j in range(4):
            board[i][j] = lines2[k][j]
        k += 1


def move():
    cnt = 0
    for i in range(4):
        if board[i][4] == 1:
            cnt += 1
            break
    for i in range(4):
        if board[i][5] == 1:
            cnt += 1
            break

    for _ in range(cnt):
        for i in range(4):
            for j in range(8, 3, -1):
                board[i][j + 1] = board[i][j]
                board[i][j] = 0

    cnt2 = 0
    for j in range(4):
        if board[4][j] == 1:
            cnt2 += 1
            break
    for j in range(4):
        if board[5][j] == 1:
            cnt2 += 1
            break

    for _ in range(cnt2):
        for i in range(8, 3, -1):
            for j in range(4):
                board[i + 1][j] = board[i][j]
                board[i][j] = 0


for block in blocks:
    put(block)
    erase()
    down()
    move()

cnt = 0
for i in range(10):
    for j in range(10):
        if board[i][j] == 1:
            cnt += 1
print(score)
print(cnt)