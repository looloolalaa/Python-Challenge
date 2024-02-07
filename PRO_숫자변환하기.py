# dp .. 시간?
def solution(x, y, n):
    dp = [float('inf') for _ in range(1000001)]

    dp[x] = 0
    for i in range(x, y + 1):
        if i + n < 1000001:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        if i * 2 < 1000001:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 < 1000001:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)

    if dp[y] == float('inf'):
        return -1
    return dp[y]