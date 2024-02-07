from collections import defaultdict, deque

N, M = map(int, input().split())
graph = defaultdict(list)
dist = [-1 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(s):
    que = deque([s])
    dist[s] = 0
    while que:
        now = que.popleft()
        for around in graph[now]:
            if dist[around] == -1:
                dist[around] = dist[now] + 1
                que.append(around)

result, min_num = -1, float('inf')
for i in range(1, N+1):
    for j in range(1, N+1):
        dist[j] = -1
    bfs(i)
    num = sum(dist[1:])

    if min_num > num:
        min_num = num
        result = i

print(result)