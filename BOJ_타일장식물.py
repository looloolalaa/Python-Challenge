# 달팽이(피보나치)
dp = [0 for _ in range(81)]
dp[1] = 1
dp[2] = 1

for i in range(3, 81):
    dp[i] = dp[i-1] + dp[i-2]

N = int(input())
print(2*(dp[N] + (dp[N-1]+dp[N])))
