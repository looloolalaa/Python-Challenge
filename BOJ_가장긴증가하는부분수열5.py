# LIS 최종, 배열 복원
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

dp = []
pos = [-1 for _ in range(N)]
for i in range(N):
    a = arr[i]
    p = bisect_left(dp, a)
    if p == len(dp):
        dp.append(a)
    else:
        dp[p] = a
    pos[i] = p

max_len = len(dp)
print(max_len)

ans = []
max_len -= 1
for i in range(N-1, -1, -1):
    if pos[i] == max_len:
        ans.append(arr[i])
        max_len -= 1

ans.reverse()
print(*ans)

# 여러 정답 부분수열 중 어떤 것인가?
# 2 5 3 4 1 6 0
# 0 1 1 2 0 3 0
# 0 3 4 6

