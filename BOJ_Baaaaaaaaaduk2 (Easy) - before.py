# 놓을 수 있는 모든 좌표에서 선택 + dfs return
from itertools import combinations

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def valid(i, j):
    return 0 <= i < N and 0 <= j < M

def willDie(tab):
    visited = [[False for _ in range(M)] for _ in range(N)]

    def dfs(i, j):
        cnt = 1
        for d in dxy:
            a, b = i+d[0], j+d[1]
            if valid(a, b):
                if tab[a][b] == 0:
                    nonlocal opened
                    opened = True
                elif tab[a][b] == 2 and not visited[a][b]:
                    visited[a][b] = True
                    cnt += dfs(a, b)
        return cnt

    die = 0
    for i in range(N):
        for j in range(M):
            if tab[i][j] == 2 and not visited[i][j]:
                opened = False
                visited[i][j] = True
                group = dfs(i, j)
                if not opened:
                    die += group

    return die


can_put = []
for i in range(N):
    for j in range(M):
        if table[i][j] == 0 and any(valid(i+d[0], j+d[1]) and table[i+d[0]][j+d[1]] == 2 for d in dxy):
            can_put.append((i, j))

print(can_put)
select = 2
if len(can_put) < 2:
    select = len(can_put)

ans = 0
for c in combinations(can_put, select):
    for p in c:
        table[p[0]][p[1]] = 1
    ans = max(ans, willDie(table))
    for p in c:
        table[p[0]][p[1]] = 0

print(ans)