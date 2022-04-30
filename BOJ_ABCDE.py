"""
원래: DFS 순서가 하나만 나오나
인접한 애들 모두 DFS 끝내고 나서 visited = False 처리 하면
모든 .. 경로 탐색?

반례(유연한 DFS)
5 5
0 1
1 3
1 2
2 3
3 4
"""
from collections import defaultdict
import sys

if __name__ == '__main__':
    N, M = map(int, input().split())
    edges = defaultdict(list)
    visited = {}

    for i in range(N):
        visited[i] = False

    for _ in range(M):
        i, j = map(int, sys.stdin.readline().rstrip().split())
        edges[i].append(j)
        edges[j].append(i)


    def dfs(v, d):
        if visited[v]:
            return
        if d == 4:
            print(1)
            exit()
        visited[v] = True
        for a in edges[v]:
            dfs(a, d + 1)
        visited[v] = False  # 주위 애들 dfs 끝나면 미방문으로 재표시 -> 갈래길에서 모든 경우 탐색 ..?


    for i in range(N):
        dfs(i, 0)
        for v in visited:
            visited[v] = False

    print(0)

