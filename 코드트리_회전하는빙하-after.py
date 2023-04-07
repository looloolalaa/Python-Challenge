# 회전 시작점과 box_size 로 돌리기
n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**n)]
levels = list(map(int, input().split()))
temp = [[0 for _ in range(2**n)] for _ in range(2**n)]
box_len = -1

def rotate_box(x, y):
    half = box_len // 2

    for i in range(x, x+half):
        for j in range(y, y+half):
            temp[i][j+half] = board[i][j]

    for i in range(x, x+half):
        for j in range(y+half, y+half*2):
            temp[i+half][j] = board[i][j]

    for i in range(x+half, x+half*2):
        for j in range(y+half, y+half*2):
            temp[i][j-half] = board[i][j]

    for i in range(x+half, x+half*2):
        for j in range(y, y+half):
            temp[i-half][j] = board[i][j]


def rotate(level):
    if level == 0:
        return

    global box_len
    box_len = 2 ** level

    for i in range(0, 2**n, box_len):
        for j in range(0, 2**n, box_len):
            rotate_box(i, j)


    for i in range(2**n):
        for j in range(2**n):
            board[i][j] = temp[i][j]

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def valid(p):
    return 0<=p[0]<2**n and 0<=p[1]<2**n

melt_temp = [[True for _ in range(2**n)] for _ in range(2**n)]
def melt():
    for i in range(2**n):
        for j in range(2**n):
            melt_temp[i][j] = True

    for i in range(2**n):
        for j in range(2**n):
            c = 0
            for d in dxy:
                a = i+d[0], j+d[1]
                if valid(a) and board[a[0]][a[1]] > 0:
                    c += 1

            if c >= 3:
                melt_temp[i][j] = False

    for i in range(2**n):
        for j in range(2**n):
            if melt_temp[i][j] and board[i][j] > 0:
                board[i][j] -= 1

def get_score():
    visited = [[False for _ in range(2**n)] for _ in range(2**n)]

    def size(p):
        visited[p[0]][p[1]] = True
        c = 1
        for d in dxy:
            a = p[0] + d[0], p[1] + d[1]
            if valid(a) and not visited[a[0]][a[1]] and board[a[0]][a[1]] != 0:
                c += size(a)
        return c

    s = 0
    group = 0
    for i in range(2**n):
        for j in range(2**n):
            s += board[i][j]

            if not visited[i][j] and board[i][j] != 0:
                group = max(group, size((i, j)))

    return s, group


for level in levels:
    rotate(level)
    melt()

total, max_group = get_score()
print(total)
print(max_group)




