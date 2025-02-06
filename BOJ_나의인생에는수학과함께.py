# 2차원 모든 길로 일단 문자열 만들어 놓기
N = int(input())
arr = [input().split() for _ in range(N)]

mini, maxi = float('inf'), -float('inf')
def dfs(i, j, res):
    if i >= N or j >= N:
        if len(res) == 2*N-1:
            global mini, maxi
            ans = int(my_eval(res))
            mini = min(mini, ans)
            maxi = max(maxi, ans)
        return


    dfs(i, j+1, res + [arr[i][j]])
    dfs(i+1, j, res + [arr[i][j]])

def my_eval(nums):
    now = nums[0]
    for i in range(1, 2*N-1, 2):
        now = str(eval(now+nums[i]+nums[i+1]))
    return now

dfs(0, 0, [])
print(maxi, mini)