# BFS 벽까지 보내기
from collections import deque

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def solution(board):
    n, m = len(board), len(board[0])

    def valid(p):
        return 0 <= p[0] < n and 0 <= p[1] < m

    start = -1, -1
    end = -1, -1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = i, j
            elif board[i][j] == 'G':
                end = i, j

    dist = [[-1 for _ in range(m)] for _ in range(n)]

    q = deque([start])
    dist[start[0]][start[1]] = 0
    while q:
        now = q.popleft()
        for d in dxy:
            a = now
            while valid(a) and board[a[0]][a[1]] != 'D':
                a = (a[0] + d[0], a[1] + d[1])
            a = a[0] - d[0], a[1] - d[1]

            if dist[a[0]][a[1]] == -1:
                dist[a[0]][a[1]] = dist[now[0]][now[1]] + 1
                q.append(a)

    return dist[end[0]][end[1]]