# 2차원 DP ( cost )
# 범위 나가는 경우 까지 생각 ....
def solution(alp, cop, problems):
    a, c = [], []
    for p in problems:
        a.append(p[0])
        c.append(p[1])
    a, c = max(a), max(c)

    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    dp = [[float('inf') for _ in range(c + 1)] for _ in range(a + 1)]
    alp, cop = min(alp, a), min(cop, c)
    dp[alp][cop] = 0

    for i in range(alp, a + 1):
        for j in range(cop, c + 1):
            can_solve = [p for p in problems if p[0] <= i and p[1] <= j]
            for can in can_solve:
                x, y = min(a, i + can[2]), min(c, j + can[3])
                dp[x][y] = min(dp[x][y], dp[i][j] + can[4])

    return dp[a][c]


if __name__ == '__main__':
    print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))