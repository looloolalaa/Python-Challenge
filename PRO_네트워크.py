"""
not visited 면 새 네트워크 DFS
"""


def solution(n, computers):
    visited = [False for _ in range(n)]

    def dfs(s):
        visited[s] = True
        for j in range(n):
            if computers[s][j] and s != j and not visited[j]:
                dfs(j)

    network = 0
    for i in range(n):
        if not visited[i]:
            network += 1
            dfs(i)

    return network


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))