# 모두 연결되어 있는 4개의 점 (까지의 거리)
from itertools import combinations, permutations

table = [list(input()) for _ in range(5)]
points = []
for i in range(5):
    for j in range(5):
        if table[i][j] == '*':
            points.append((i, j))
N = len(points)

dxy = [[0,1], [1,0], [0,-1], [-1,0]]
def all_connected(ps):
    # [(0,0), (0,1), (0,3)]
    element = ps[0]
    s = set(ps)

    def erase(p):
        if p not in s:
            return
        s.remove(p)

        for d in dxy:
            a = p[0]+d[0], p[1]+d[1]
            erase(a)

    erase(element)
    return len(s) == 0

def dist(ps):
    return sum(abs(a[0]-b[0])+abs(a[1]-b[1]) for a, b in zip(ps, points))

ans = float('inf')
for com in combinations(range(25), N):
    ps = [(idx//5, idx%5) for idx in com]
    if all_connected(ps):
        for p in permutations(ps, N):
            ans = min(ans, dist(p))

print(ans)