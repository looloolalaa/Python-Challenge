# 두 점에서 동시에 십자가 최대로 늘리기
from itertools import combinations

N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]

points = []
for i in range(N):
    for j in range(M):
        if table[i][j] == '#':
            points.append((i, j))

dxy = [[0,1], [1,0], [0,-1], [-1,0]]
def valid(p):
    return 0<=p[0]<N and 0<=p[1]<M

def spanning(a, b):
    visited_a = {a}
    visited_b = {b}
    dist_a, dist_b = 1, 1
    while True:
        next_a = set()
        for d in dxy:
            p = a[0]+d[0]*dist_a, a[1]+d[1]*dist_a
            if valid(p) and table[p[0]][p[1]] == '#':
                next_a.add(p)

        next_b = set()
        for d in dxy:
            p = b[0] + d[0] * dist_b, b[1] + d[1] * dist_b
            if valid(p) and table[p[0]][p[1]] == '#':
                next_b.add(p)

        if len(next_a) < 4 or len(next_b) < 4 or next_a & next_b or next_a & visited_b or next_b & visited_a:
            break

        visited_a |= next_a
        visited_b |= next_b
        dist_a += 1
        dist_b += 1

    while True:
        next_a = set()
        for d in dxy:
            p = a[0] + d[0] * dist_a, a[1] + d[1] * dist_a
            if valid(p) and table[p[0]][p[1]] == '#':
                next_a.add(p)

        if len(next_a) < 4 or next_a & visited_b:
            break
        visited_a |= next_a
        dist_a += 1

    while True:
        next_b = set()
        for d in dxy:
            p = b[0] + d[0] * dist_b, b[1] + d[1] * dist_b
            if valid(p) and table[p[0]][p[1]] == '#':
                next_b.add(p)

        if len(next_b) < 4 or next_b & visited_a:
            break
        visited_b |= next_b
        dist_b += 1

    return [dist_a, dist_b]


ans = 0
for a, b in combinations(points, 2):
    dist_a, dist_b = spanning(a, b)
    size_a, size_b = 4 * (dist_a - 1) + 1, 4 * (dist_b - 1) + 1
    ans = max(ans, size_a * size_b)

print(ans)


