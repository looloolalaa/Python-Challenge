# product -> dfs
N, S = map(int, input().split())
arr = list(map(int, input().split()))

res = 0
def dfs(i, s):
    if i == N:
        if s == S:
            global res
            res += 1
        return

    dfs(i+1, s)
    dfs(i+1, s+arr[i])

dfs(0, 0)

if S == 0:
    res -= 1
print(res)