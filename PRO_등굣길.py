"""
DP
road[i][j] += road[i-1][j] + road[i][j-1]
"""


def solution(m, n, puddles):
    road = [[0 for _ in range(m)] for _ in range(n)]

    for j in range(m):
        if [j + 1, 1] in puddles:
            break
        road[0][j] = 1

    for i in range(n):
        if [1, i + 1] in puddles:
            break
        road[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if [j + 1, i + 1] in puddles:
                continue
            road[i][j] += road[i - 1][j] + road[i][j - 1]

    # print(road)
    return road[-1][-1] % 1000000007


if __name__ == '__main__':
    print(solution(4, 3, [[2, 2]]))