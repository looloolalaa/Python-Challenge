# 2차원 dp
dp = [1 for _ in range(10)]
ans = [0]
for _ in range(65):
    ans.append(sum(dp))

    new_dp = [0 for _ in range(10)]
    for i in range(10):
        for j in range(i, 10):
            new_dp[j] += dp[i]
    dp = new_dp


for _ in range(int(input())):
    n = int(input())
    print(ans[n])