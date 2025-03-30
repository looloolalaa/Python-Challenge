# 연산자 개수로 dfs
n = int(input())
nums = list(map(int, input().split()))
a,b,c = map(int, input().split())

mini, maxi = int(1e9), -int(1e9)
def dfs(depth, res, a,b,c):
    if depth == n:
        global mini, maxi
        mini = min(mini, res)
        maxi = max(maxi, res)
        return

    if a > 0:
        dfs(depth+1, res + nums[depth], a-1,b,c)
    if b > 0:
        dfs(depth+1, res - nums[depth], a,b-1,c)
    if c > 0:
        dfs(depth+1, res * nums[depth], a,b,c-1)

dfs(1, nums[0], a,b,c)
print(mini, maxi)