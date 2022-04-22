"""
다익스트라
"""


from collections import defaultdict
import heapq


def solution(n, edge):

    graph = defaultdict(dict)
    for s, e in edge:
        graph[s][e] = 1
        graph[e][s] = 1

    def dijkstra(graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0 
        queue = []
        heapq.heappush(queue, [distances[start], start])

        while queue:
            current_distance, current_destination = heapq.heappop(queue)

            if distances[current_destination] < current_distance:
                continue

            for new_destination, new_distance in graph[current_destination].items():
                distance = current_distance + new_distance
                if distance < distances[new_destination]:
                    distances[new_destination] = distance
                    heapq.heappush(queue, [distance, new_destination])

        return distances

    shortest = dijkstra(graph, 1)
    max_dis = max(shortest.values())
    count = 0
    for v, d in shortest.items():
        if d == max_dis:
            count += 1

    return count


if __name__ == '__main__':
    print()