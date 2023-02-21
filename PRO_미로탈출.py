# def bfs
from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])

    def valid(p):
        return 0 <= p[0] < n and 0 <= p[1] < m

    dxy = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    s, l, e = (-1, -1), (-1, -1), (-1, -1)
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                s = (i, j)
            if maps[i][j] == 'L':
                l = (i, j)
            if maps[i][j] == 'E':
                e = (i, j)

    dis = [[-1 for _ in range(m)] for _ in range(n)]

    def bfs(start):
        for i in range(n):
            for j in range(m):
                dis[i][j] = -1

        q = deque([start])
        dis[start[0]][start[1]] = 0
        while q:
            now = q.popleft()
            for d in dxy:
                a = (now[0] + d[0], now[1] + d[1])
                if valid(a) and maps[a[0]][a[1]] != 'X' and dis[a[0]][a[1]] == -1:
                    dis[a[0]][a[1]] = dis[now[0]][now[1]] + 1
                    q.append(a)

    bfs(s)
    l_dis = dis[l[0]][l[1]]

    bfs(l)
    e_dis = dis[e[0]][e[1]]

    if l_dis == -1 or e_dis == -1:
        return -1
    return l_dis + e_dis


if __name__ == '__main__':
    print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))