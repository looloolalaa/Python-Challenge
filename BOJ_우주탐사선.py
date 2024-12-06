# 중복 방문 최단 거리(플로이드-워셜)
from itertools import permutations

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

def dist(order):
    d = 0
    for i in range(len(order)-1):
        d += graph[order[i]][order[i+1]]
    return d

planets = [i for i in range(N)]
planets.remove(K)

ans = float('inf')
for p in permutations(planets, len(planets)):
    order = [K] + list(p)
    ans = min(ans, dist(order))

print(ans)
