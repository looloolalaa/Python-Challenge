# 3개 연속 선택 불가능
import sys
input = sys.stdin.readline

n = int(input())
arr = [0,0,0] + [int(input()) for _ in range(n)]

dp = [0 for _ in range(n+3)]

for i in range(3, n+3):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

print(dp[-1])

# i-3 i-2 i-1 i
