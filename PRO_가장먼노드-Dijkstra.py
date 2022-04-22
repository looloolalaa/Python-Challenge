from collections import defaultdict
import heapq

"""
Dijkstra:
힙에서 뺀 놈의 
주위 애들 중 
갱신될 수 있는 애들만
!갱신 하고 힙에 박기! 
"""


def solution(n, edge):
    graph = defaultdict(dict)
    dis = {}
    h = []

    for e in edge:
        graph[e[0]][e[1]] = 1
        graph[e[1]][e[0]] = 1

    for i in range(1, n+1):
        dis[i] = float('inf')


    def dijkstra(s):
        dis[s] = 0
        heapq.heappush(h, (0, s))

        while h:
            d, v = heapq.heappop(h)
            if dis[v] < d:
                continue

            for a in graph[v]:
                new_dis = d + graph[v][a]
                if dis[a] > new_dis:
                    dis[a] = new_dis
                    heapq.heappush(h, (new_dis, a))


    dijkstra(1)
    # print(dis)
    max_len = max(dis.values())

    count = 0
    for d in dis.values():
        if d == max_len:
            count += 1

    return count


if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))