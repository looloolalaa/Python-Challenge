# 십자가 출구 dfs
import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
table = [[0 for _ in range(C)] for _ in range(R + 3)]

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def valid(p):
    return 0 <= p[0] < R + 3 and 0 <= p[1] < C


def get_pos(c, d):
    i, j = 1, c - 1
    dd = 0

    def move():
        nonlocal i, j, dd

        down_pos = [(i + 2, j), (i + 1, j - 1), (i + 1, j + 1)]
        if all(valid(p) and table[p[0]][p[1]] == 0 for p in down_pos):
            i += 1
            return True

        left_pos = [(i, j - 2), (i - 1, j - 1), (i + 1, j - 1), (i + 2, j - 1), (i + 1, j - 2)]
        if all(valid(p) and table[p[0]][p[1]] == 0 for p in left_pos):
            i += 1
            j -= 1
            dd -= 1
            return True

        right_pos = [(i, j + 2), (i - 1, j + 1), (i + 1, j + 1), (i + 2, j + 1), (i + 1, j + 2)]
        if all(valid(p) and table[p[0]][p[1]] == 0 for p in right_pos):
            i += 1
            j += 1
            dd += 1
            return True

        return False

    while move():
        pass

    return i, j, dd


def init():
    for i in range(R + 3):
        for j in range(C):
            table[i][j] = 0


visited = set()
deepest = 0


def dfs(p):
    global deepest

    num = table[p[0]][p[1]]
    if num > 0:
        for d in dxy:
            a = p[0] + d[0], p[1] + d[1]
            if valid(a) and a not in visited and table[a[0]][a[1]] in (num, -num):
                visited.add(a)
                deepest = max(deepest, a[0])
                dfs(a)
    elif num < 0:
        for d in dxy:
            a = p[0] + d[0], p[1] + d[1]
            if valid(a) and a not in visited and table[a[0]][a[1]] != 0:
                visited.add(a)
                deepest = max(deepest, a[0])
                dfs(a)


ans = 0
for num in range(1, K + 1):
    c, d = map(int, input().split())

    i, j, dd = get_pos(c, d)
    if i <= 3:
        init()
        continue

    table[i][j] = num
    for di in dxy:
        a, b = i + di[0], j + di[1]
        table[a][b] = num

    d = (d + dd) % 4
    table[i + dxy[d][0]][j + dxy[d][1]] *= -1

    visited = set((i, j))
    deepest = i
    dfs((i, j))
    ans += deepest - 2

print(ans)
