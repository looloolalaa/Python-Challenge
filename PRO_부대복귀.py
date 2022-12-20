# BFS 최단거리
from collections import deque, defaultdict


def solution(n, roads, sources, destination):
    graph = defaultdict(set)
    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)

    dis = [-1 for _ in range(n + 1)]
    dis[destination] = 0

    que = deque([destination])
    while que:
        now = que.popleft()
        for a in graph[now]:
            if dis[a] == -1:
                dis[a] = dis[now] + 1
                que.append(a)

    return [dis[i] for i in sources]


if __name__ == '__main__':
    print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))