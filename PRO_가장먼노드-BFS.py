"""
모든 간선의 길이가 같으면 BFS 사용 가능
visited, dis
"""


from collections import defaultdict, deque


def solution(n, edge):
    graph = defaultdict(list)
    visited = set()
    dis = {}

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    for i in range(1, n+1):
        dis[i] = float('inf')

    def bfs(s):
        que = deque()

        que.append(s)
        visited.add(s)
        dis[s] = 0
        while que:
            now = que.popleft()
            for a in graph[now]:
                if a not in visited:
                    que.append(a)
                    visited.add(a)
                    dis[a] = dis[now] + 1

    bfs(1)
    long = max(dis.values())

    count = 0
    for d in dis.values():
        if d == long:
            count += 1

    return count


if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))