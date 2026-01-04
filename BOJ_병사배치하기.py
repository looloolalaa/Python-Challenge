# LIS 최장증가부분수열
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

dp = []
for i in range(N-1, -1, -1):
    p = bisect_left(dp, arr[i])
    if p == len(dp):
        dp.append(arr[i])
    else:
        dp[p] = arr[i]

print(N - len(dp))