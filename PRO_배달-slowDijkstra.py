# greedy(O(n**2)) 다익스트라
from collections import defaultdict


def solution(N, road, K):
    graph = defaultdict(dict)
    for a, b, c in road:
        graph[a].setdefault(b, float('inf'))
        graph[b].setdefault(a, float('inf'))
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)

    dis = [float('inf') for _ in range(N + 1)]
    not_visited = set(i for i in range(1, N + 1))

    dis[1] = 0
    while not_visited:
        min_v = min(not_visited, key=lambda x: dis[x])
        not_visited.remove(min_v)

        for a in graph[min_v]:
            if a in not_visited:
                dis[a] = min(dis[a], dis[min_v] + graph[min_v][a])

    # print(dis)
    return len(list(filter(lambda x: x <= K, dis)))


if __name__ == '__main__':
    print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))