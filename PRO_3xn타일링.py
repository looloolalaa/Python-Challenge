# dp 점화식
def solution(n):
    dp = [0 for _ in range(5001)]
    s = [0 for _ in range(5001)]
    dp[0] = 1
    dp[2] = 3

    s[0] = 1
    s[2] = s[0] + dp[2]

    for i in range(4, 5001, 2):
        dp[i] = dp[i - 2] * 3 + s[i - 4] * 2
        s[i] = s[i - 2] + dp[i]

    return dp[n] % 1_000_000_007