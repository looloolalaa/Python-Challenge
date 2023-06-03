# 구현 - combinations 경우의 수
from itertools import combinations

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus = []
zeros = []


dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < m

def safe_area(boa):
    def dfs(s):
        for d in dxy:
            a = s[0]+d[0], s[1]+d[1]
            if valid(a) and boa[a[0]][a[1]] == 0:
                boa[a[0]][a[1]] = 2
                dfs(a)

    for v in virus:
        dfs(v)

    count = 0
    for i in range(n):
        for j in range(m):
            if boa[i][j] == 0:
                count += 1
    return count




for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus.append((i, j))
        elif board[i][j] == 0:
            zeros.append((i, j))

candis = list(combinations(zeros, 3))

maxi = 0
for can in candis:
    new_board = [line[:] for line in board]
    for i, j in can:
        new_board[i][j] = 1
    maxi = max(maxi, safe_area(new_board))

print(maxi)