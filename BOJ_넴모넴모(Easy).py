N, M = map(int, input().split())
arr = [[0 for _ in range(M+1)] for _ in range(N+1)]

ans = 0
def dfs(idx):
    if idx == N*M:
        global ans
        ans += 1
        return

    i, j = idx//M+1, idx%M+1
    arr[i][j] = 0
    dfs(idx+1)

    if arr[i-1][j] == 0 or arr[i][j-1] == 0 or arr[i-1][j-1] == 0:
        arr[i][j] = 1
        dfs(idx+1)

dfs(0)
print(ans)