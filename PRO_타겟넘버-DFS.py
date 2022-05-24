"""
DFS
"""


def solution(numbers, target):
    def dfs(i, s):
        if i == len(numbers):
            return 1 if s == target else 0
        return dfs(i + 1, s + numbers[i]) + dfs(i + 1, s - numbers[i])

    return dfs(0, 0)


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))