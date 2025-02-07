# 비트마스킹 + dp
N, M = map(int, input().split())
N, M = max(N, M), min(N, M)

# dp[idx][state]
# == idx번째 칸을 기준으로 이전 M+1 개의 칸의 상태가 state일 때
# idx 이후 모든 칸을 채우는 경우의 수

dp = [[0 for _ in range(2**(M+1))] for _ in range(N*M)]
MOD = 1_000_000_007

def get_dp(idx, state):
    if idx == N*M:
        return 1

    if dp[idx][state] != 0:
        return dp[idx][state] % MOD

    if idx % M != 0 and (state & 1) != 0 and (state & 2) != 0 and (state & (1<<M)) != 0:
        dp[idx][state] = get_dp(idx+1, state>>1) % MOD
    else:
        dp[idx][state] = get_dp(idx+1, state>>1) % MOD + get_dp(idx+1, (state>>1) | (1<<M)) % MOD

    return dp[idx][state] % MOD

print(get_dp(0, 0))
