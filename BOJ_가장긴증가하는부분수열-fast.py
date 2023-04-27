# 최장 증가 수열(LIS) - O(NlogN)
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

dp = []

for a in arr:
    i = bisect_left(dp, a)
    if i == len(dp):
        dp.append(a)
    else:
        dp[i] = min(dp[i], a)


print(len(dp))
