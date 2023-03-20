# BFS
# def 
from collections import deque

n = int(input())
table = [input() for _ in range(n)]
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def valid(p):
    return (0 <= p[0] < n and 0 <= p[1] < n) and table[p[0]][p[1]] != '#'


def total_dist(order):
    a, b, c, d = dist('S', order[0]), dist(order[0], order[1]), dist(order[1], order[2]), dist(order[2], 'E')
    if a == -1 or b == -1 or c == -1 or d == -1:
        return -1
    return a + b + c + d


def dist(s, e):
    sp = (-1, -1)
    ep = (-1, -1)
    for i in range(n):
        for j in range(n):
            if table[i][j] == s:
                sp = (i, j)
            if table[i][j] == e:
                ep = (i, j)

    dis = [[-1 for _ in range(n)] for _ in range(n)]
    dis[sp[0]][sp[1]] = 0
    q = deque()
    q.append(sp)

    while q:
        now = q.popleft()
        for d in dxy:
            a = (now[0] + d[0], now[1] + d[1])
            if valid(a) and dis[a[0]][a[1]] == -1:
                dis[a[0]][a[1]] = dis[now[0]][now[1]] + 1
                q.append(a)

    return dis[ep[0]][ep[1]]


def combinations(cards, m):
    # cards == ['1', '2', '3', '4', '5']
    result = []
    temp = ['0' for _ in range(m)]

    def dfs(i, j):
        if j == m:
            result.append(temp.copy())
            return
        for k in range(i, len(cards)):
            temp[j] = cards[k]
            dfs(k + 1, j + 1)

    dfs(0, 0)
    return result


numbers = []
for i in range(n):
    for j in range(n):
        if '1' <= table[i][j] <= '9':
            numbers.append(table[i][j])
numbers.sort()

if len(numbers) < 3:
    print(-1)
    exit()

candis = combinations(numbers, 3)
all_dist = []
for c in candis:
    d = total_dist(c)
    if d != -1:
        all_dist.append(d)

print(min(all_dist) if all_dist else -1)