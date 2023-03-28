# 부분 회전 + 컬러링(coloring) dfs
from collections import defaultdict

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
colored = [[-1 for _ in range(n)] for _ in range(n)]
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def valid(p):
    return 0<=p[0]<n and 0<=p[1]<n

book = {}

def coloring():
    book.clear()
    for i in range(n):
        for j in range(n):
            colored[i][j] = -1

    def dfs(p, c):
        colored[p[0]][p[1]] = c
        for d in dxy:
            a = p[0]+d[0], p[1]+d[1]
            if valid(a) and table[p[0]][p[1]] == table[a[0]][a[1]] and colored[a[0]][a[1]] == -1:
                dfs(a, c)

    color = 1
    for i in range(n):
        for j in range(n):
            if colored[i][j] == -1:
                book[color] = table[i][j]
                dfs((i, j), color)
                color += 1


def score():
    coloring()

    near = defaultdict(int)
    counter = defaultdict(int)
    for i in range(n):
        for j in range(n):
            counter[colored[i][j]] += 1
            for d in dxy:
                a = i+d[0],j+d[1]
                if valid(a) and colored[i][j] < colored[a[0]][a[1]]:
                    near[(colored[i][j], colored[a[0]][a[1]])] += 1

    total = 0
    for a, b in near:
        total += (counter[a] + counter[b]) * book[a] * book[b] * near[(a, b)]
    return total

def rotated(arr):
    return list(zip(*arr[::-1]))

def rotate():
    # +
    temp = [row[:] for row in table]
    for _ in range(3):
        temp = rotated(temp)

    for j in range(n):
        table[n//2][j] = temp[n//2][j]
    for i in range(n):
        table[i][n//2] = temp[i][n//2]

    # 1
    rect = [[-1 for _ in range(n//2)] for _ in range(n//2)]
    for i in range(n//2):
        for j in range(n//2):
            rect[i][j] = table[i][j]

    rect = rotated(rect)
    for i in range(n//2):
        for j in range(n//2):
            table[i][j] = rect[i][j]

    # 2
    rect = [[-1 for _ in range(n//2)] for _ in range(n//2)]
    for i in range(n//2):
        for j in range((n//2)+1, n):
            rect[i][j - (n//2)-1] = (table[i][j])

    rect = rotated(rect)
    for i in range(n//2):
        for j in range((n//2)+1, n):
            (table[i][j]) = rect[i][j - (n//2)-1]

    # 3
    rect = [[-1 for _ in range(n//2)] for _ in range(n//2)]
    for i in range(n//2+1, n):
        for j in range(n//2):
            rect[i - (n//2)-1][j] = (table[i][j])

    rect = rotated(rect)
    for i in range(n//2+1, n):
        for j in range(n//2):
            (table[i][j]) = rect[i - (n//2)-1][j]

    # 4
    rect = [[-1 for _ in range(n//2)] for _ in range(n//2)]
    for i in range((n//2)+1, n):
        for j in range((n//2)+1, n):
            rect[i- (n//2)-1][j - (n//2)-1] = (table[i][j])

    rect = rotated(rect)
    for i in range((n//2)+1, n):
        for j in range((n//2)+1, n):
            (table[i][j]) = rect[i- (n//2)-1][j - (n//2)-1]


result = 0
for _ in range(4):
    result += score()
    rotate()
print(result)