# 좌표 선택
from itertools import combinations

arr = [input() for _ in range(5)]

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def valid(order):
    cnt = 0
    for p in order:
        if arr[p[0]][p[1]] == 'S':
            cnt += 1

    if cnt < 4:
        return False

    visited = [False for _ in range(7)]

    def dfs(i):
        for j in range(7):
            if i != j and not visited[j]:
                if dist(order[i], order[j]) == 1:
                    visited[j] = True
                    dfs(j)


    visited[0] = True
    dfs(0)

    return all(v for v in visited)

pos = []
for i in range(5):
    for j in range(5):
        pos.append((i, j))

ans = 0
for candi in combinations(pos, 7):
    if valid(candi):
        ans += 1
print(ans)
