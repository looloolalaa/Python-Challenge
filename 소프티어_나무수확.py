# dp: 위경로 + 아래경로
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
rdp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + arr[i-1][j-1]

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        rdp[i][j] = max(rdp[i+1][j], rdp[i][j+1]) + arr[i][j]

ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        ans = max(ans, dp[i][j] + rdp[i-1][j-1])
print(ans)