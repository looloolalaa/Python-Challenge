# 완전탐색
from itertools import combinations


N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if table[i][j] == 1:
            houses.append((i, j))
        if table[i][j] == 2:
            chickens.append((i, j))

def dist(chi):
    res = 0
    for h in houses:
        chi_dist = min(abs(c[0]-h[0]) + abs(c[1]-h[1]) for c in chi)
        res += chi_dist
    return res


print(min(dist(candi) for candi in combinations(chickens, M)))
