# 경우의수(조합)들 중 최대값
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

temp = [-1 for _ in range(3)]
cards = []
fires = []
for i in range(n):
    for j in range(m):
        if table[i][j] == 0:
            cards.append((i, j))
        if table[i][j] == 2:
            fires.append((i, j))

candis = []
def dfs(i, j):
    if j == 3:
        new_table = [t[:] for t in table]

        for x, y in temp:
            new_table[x][y] = 1

        fire(new_table)
        candis.append(safe_area())
        return

    for k in range(i, len(cards)):
        temp[j] = cards[k]
        dfs(k+1, j+1)



dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def valid(p):
    return 0<=p[0]<n and 0<=p[1]<m

board = [[-1 for _ in range(m)] for _ in range(n)]
def fire(tab):
    global board
    for i in range(n):
        for j in range(m):
            board[i][j] = tab[i][j]

    def spread(p):
        board[p[0]][p[1]] = 2
        for d in dxy:
            a = p[0]+d[0], p[1]+d[1]
            if valid(a) and board[a[0]][a[1]] == 0:
                spread(a)

    for x, y in fires:
        spread((x, y))


def safe_area():
    global board
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count += 1
    return count

dfs(0, 0)
print(max(candis))