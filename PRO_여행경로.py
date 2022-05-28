"""
Stack
"""
from collections import defaultdict


def solution(tickets):
    answer = []
    graph = defaultdict(list)

    for a, b in tickets:
        graph[a].append(b)
    for v in graph:
        graph[v].sort(reverse=True)  # 'A': ['C', 'B']
    print(graph)

    stack = ['ICN']
    while stack:
        now = stack[-1]
        if not graph[now]:  # 막다른 길이면
            answer.append(stack.pop())  # answer 에 추가
        else:  # 더 갈 수 있는 곳이 있으면
            stack.append(graph[now].pop())  # stack 에 추가

    answer.reverse()
    return answer


if __name__ == '__main__':
    print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))