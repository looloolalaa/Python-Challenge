# LIS 응용
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

dp = []
for a in arr:
    i = bisect_left(dp, a)
    if i == len(dp):
        dp.append(a)
    else:
        dp[i] = a

print(len(dp))