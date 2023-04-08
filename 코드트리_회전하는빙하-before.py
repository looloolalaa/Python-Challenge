# 좌표 옮기기 (테스트하기 쉽게 나눠서)
n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**n)]
levels = list(map(int, input().split()))

def rotated(arr):
    m = len(arr)
    half = m // 2
    temp = [[0 for _ in range(m)] for _ in range(m)]

    for i in range(m):
        for j in range(m):
            if i < half and j < half:
                temp[i][j+half] = arr[i][j]
            if i < half and j >= half:
                temp[i+half][j] = arr[i][j]
            if i >= half and j >= half:
                temp[i][j-half] = arr[i][j]
            if i >= half and j < half:
                temp[i - half][j] = arr[i][j]

    return temp


def rotate(level):
    if level == 0:
        return

    box_len = 2 ** level
    target = [[0 for _ in range(2 ** level)] for _ in range(2 ** level)]

    for i in range(0, 2**n, box_len):
        for j in range(0, 2**n, box_len):

            for x in range(i, i + 2 ** level):
                for y in range(j, j + 2 ** level):
                    target[x - i][y - j] = board[x][y]

            rotated_target = rotated(target)
            for x in range(i, i + 2 ** level):
                for y in range(j, j + 2 ** level):
                    board[x][y] = rotated_target[x - i][y - j]

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




