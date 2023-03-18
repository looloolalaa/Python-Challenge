# 2차원 배열 컬러링
n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

a = -1, -1
b = -1, -1
for i in range(n):
    for j in range(n):
        if table[i][j] == 2:
            a = i, j
        if table[i][j] == 3:
            b = i, j


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def size(p):
    if table[p[0]][p[1]] == 0:
        return 0

    s = 1
    table[p[0]][p[1]] = 0
    for d in dxy:
        a = p[0] + d[0], p[1] + d[1]
        if valid(a):
            s += size(a)
    return s


print(size(a), size(b))