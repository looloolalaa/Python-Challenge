# dp 안의 dp 이용하기
N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [int(1e9) for _ in range(N+1)]
dp[0] = 0

for n in range(1, N+1):
    for i in range(0, n+1):
        dp[n] = min(dp[n], arr[i] + dp[n-i])

print(dp[N])