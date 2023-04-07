# dfs coloring (그룹묶기) + 돌까지 내리는 중력

# 같은 그룹에 속한 좌표들을 먼저 체킹 후 bundle 구하기
# remove 또한 체킹 후 삭제하는 방법
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def valid(p):
    return 0<=p[0]<n and 0<=p[1]<n


def dfs(p, color):
    visited[p[0]][p[1]] = True
    bomb = 1
    red_bomb = 1 if board[p[0]][p[1]] == 0 else 0
    point = p
    for d in dxy:
        a = p[0]+d[0],p[1]+d[1]
        if valid(a) and not visited[a[0]][a[1]] and (color == board[a[0]][a[1]] or 0 == board[a[0]][a[1]]):
            bo, re, po = dfs(a, color)
            bomb += bo
            red_bomb += re
            if board[po[0]][po[1]] != 0:
                if (point[0], -point[1]) < (po[0], -po[1]):
                    point = po
    return (bomb, red_bomb, point)

def red_init():
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                visited[i][j] = False


candis = {}
def get_candis():
    candis.clear()
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    for i in range(n):
        for j in range(n):
            if 1 <= board[i][j] <= m and not visited[i][j]:
                red_init()
                bo, re, po = dfs((i, j), board[i][j])
                if bo >= 2:
                    candis[(i, j)] = (bo, re, po)


def remove(p, color):
    board[p[0]][p[1]] = -2
    for d in dxy:
        a = p[0]+d[0], p[1]+d[1]
        if valid(a) and board[a[0]][a[1]] != -2 and (board[a[0]][a[1]] == color or board[a[0]][a[1]] == 0):
            remove(a, color)


def gravity():
    temp = [[-2 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        stone = n - 1
        for i in range(n-1, -1, -1):
            if board[i][j] == -2:
                continue
            if board[i][j] == -1:
                stone = i
            temp[stone][j] = board[i][j]
            stone -= 1

    for i in range(n):
        for j in range(n):
            board[i][j] = temp[i][j]

def rotated(arr):
    return list(zip(*arr[::-1]))

def rotate():
    global board

    temp = [row[:] for row in board]
    for _ in range(3):
        temp = rotated(temp)
    for i in range(n):
        for j in range(n):
            board[i][j] = temp[i][j]

score = 0
while True:
    get_candis()
    if not candis:
        break

    target = max(candis, key=lambda x: (candis[x][0], -candis[x][1], candis[x][2][0], -candis[x][2][1]))
    C = candis[target][0]
    score += C * C
    remove(target, board[target[0]][target[1]])
    gravity()
    rotate()
    gravity()


print(score)
# for b in board:
#     print(b)

# (폭탄개수, 빨간폭탄개수, 기준점)


