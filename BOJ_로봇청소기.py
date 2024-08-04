# dfs 안에서 2차반복 X
from collections import deque
import sys
input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = [list(input()) for _ in range(h)]

    def valid(p):
        return 0 <= p[0] < h and 0 <= p[1] < w
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def get_dist(p):
        dist = [[-1 for _ in range(w)] for _ in range(h)]
        dist[p[0]][p[1]] = 0
        que = deque([p])
        while que:
            now = que.popleft()
            for d in dxy:
                a = now[0]+d[0], now[1]+d[1]
                if valid(a) and board[a[0]][a[1]] != 'x' and dist[a[0]][a[1]] == -1:
                    dist[a[0]][a[1]] = dist[now[0]][now[1]] + 1
                    que.append(a)
        return dist

    dists = {}
    start = -1, -1
    trash = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'o':
                start = i, j
                dists[(i, j)] = get_dist((i, j))
            if board[i][j] == '*':
                trash.append((i, j))
                dists[(i, j)] = get_dist((i, j))

    ans = float('inf')

    def dfs(depth, p, d):
        global ans
        if ans == -1:
            return
        if ans <= d:
            return
        if depth == len(trash):
            ans = min(ans, d)
            return

        dist = dists[p]
        for a, b in trash:
            if board[a][b] == '*':
                if dist[a][b] == -1:
                    ans = -1
                    return

                board[p[0]][p[1]] = '.'
                board[a][b] = 'o'
                dfs(depth+1, (a, b), d+dist[a][b])
                board[a][b] = '*'
                board[p[0]][p[1]] = 'o'

    dfs(0, start, 0)
    print(ans)
