# O(nlogn) 다익스트라
from collections import defaultdict
import heapq


def solution(N, road, K):
    graph = defaultdict(dict)
    for a, b, c in road:
        graph[a].setdefault(b, float('inf'))
        graph[b].setdefault(a, float('inf'))
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)

    dis = [float('inf') for _ in range(N + 1)]

    dis[1] = 0
    h = [(0, 1)]
    while h:
        d, n = heapq.heappop(h)
        if d > dis[n]:
            continue

        for a in graph[n]:
            new_d = dis[n] + graph[n][a]
            if new_d < dis[a]:
                dis[a] = new_d
                heapq.heappush(h, (new_d, a))

    return len(list(filter(lambda x: x <= K, dis)))


if __name__ == '__main__':
    print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))