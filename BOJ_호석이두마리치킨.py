# 플로이드워셜 + 2지점 선택
from itertools import combinations

N, M = map(int, input().split())
graph = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

def total_dist(chicken1, chicken2):
    total = 0
    for i in range(1, N+1):
        total += min(graph[i][chicken1], graph[i][chicken2])
    return 2 * total

ans, ans_dist = (-1, -1), float('inf')
for chicken1, chicken2 in combinations(range(1, N+1), 2):
    total = total_dist(chicken1, chicken2)
    if ans_dist > total:
        ans = chicken1, chicken2
        ans_dist = total

print(ans[0], ans[1], ans_dist)
