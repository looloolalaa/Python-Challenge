"""
노드 i가 순위를 매길 수 있으려면
i를 제외한 나머지 모든 노드와 승패를 가릴 수 있어야 함.
-> n-1 개

플로이드-워셜 변형:
i가 k를 이기고 k가 j를 이기면
i가 j를 이긴다.
"""


def solution(n, results):
    graph = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    for a, b in results:
        graph[a][b] = True

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

    def can_rank(node):
        win_or_lose = 0
        for j in range(1, n + 1):
            if graph[node][j] or graph[j][node]:
                win_or_lose += 1
        return win_or_lose == n - 1

    answer = 0
    for i in range(1, n + 1):
        if can_rank(i):
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))