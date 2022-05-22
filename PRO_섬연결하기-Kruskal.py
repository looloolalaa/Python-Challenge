"""
MST - Kruskal
Greedy
"""
from collections import deque


# Union-Find
def solution(n, costs):
    edge_count = 0
    costs = deque(sorted(costs, key=lambda x: x[2]))
    parents = [i for i in range(n)]
    # Root: i == parents[i]

    # Find: 경로 압축
    def root(i):
        if parents[i] != i:
            parents[i] = root(parents[i])
        return parents[i]

    total_cost = 0

    # MST: len(edges) == n-1
    while edge_count < n - 1:
        a, b, c = costs.popleft()
        root_a, root_b = root(a), root(b)
        if root_a != root_b:
            edge_count += 1
            # Union: 1 <- 3
            parents[max(root_a, root_b)] = min(root_a, root_b)
            total_cost += c
            # print(parents)

    return total_cost


if __name__ == '__main__':
    print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))