# 리프노드의 반대편 노드를 선택
from collections import defaultdict


def solution(n, lighthouse):
    graph = defaultdict(set)
    for a, b in lighthouse:
        graph[a].add(b)
        graph[b].add(a)

    leaves = set()
    for i in graph:
        if len(graph[i]) == 1:
            leaves.add(i)

    result = set()
    while leaves:
        leaf = leaves.pop()
        if len(graph[leaf]) != 1:
            continue

        selected = list(graph[leaf])[0]
        result.add(selected)

        adj = graph[selected].copy()
        for a in adj:
            graph[a].remove(selected)
            graph[selected].remove(a)
            if len(graph[a]) == 1:
                leaves.add(a)

    # print(result)
    return len(result)


if __name__ == '__main__':
    print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))