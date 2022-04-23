"""
Graph DFS, BFS
"""


import sys
from collections import defaultdict, deque

if __name__ == '__main__':
    graph = defaultdict(list)
    visited = {}

    N, M, V = map(int, input().split())
    for _ in range(M):
        i, j = map(int, sys.stdin.readline().rstrip().split())
        graph[i].append(j)
        graph[j].append(i)

    for i in range(1, N+1):
        visited[i] = False

    for k in graph:
        graph[k].sort()

    def dfs(v):
        if visited[v]:
            return
        print(v, end=' ')
        visited[v] = True
        for a in graph[v]:
            dfs(a)

    def bfs(v):
        que = deque()
        que.append(v)
        while que:
            n = que.popleft()
            if visited[n]:
                continue
            print(n, end=' ')
            visited[n] = True
            for a in graph[n]:
                que.append(a)


    dfs(V)
    print()
    for v in visited:
        visited[v] = False
    bfs(V)
    print()
    # print(graph)