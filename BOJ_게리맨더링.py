# 선거구 색깔 나누기
from collections import defaultdict
from itertools import product

N = int(input())
people = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(N):
    graph[i+1] += list(map(int, input().split()))[1:]


ans = float('inf')
for color in product([0, 1], repeat=N):
    color = [-1] + list(color)
    visited = [False for _ in range(N + 1)]
    red_blue = [0, 0]

    def dfs(i):
        for a in graph[i]:
            if not visited[a] and color[a] == color[i]:
                visited[a] = True
                dfs(a)

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            red_blue[color[i]] += 1
            dfs(i)

    if red_blue == [1, 1]:
        red_blue_people = [0, 0]
        for i in range(1, N+1):
            red_blue_people[color[i]] += people[i-1]
        ans = min(ans, abs(red_blue_people[0]-red_blue_people[1]))

print(-1 if ans == float('inf') else ans)