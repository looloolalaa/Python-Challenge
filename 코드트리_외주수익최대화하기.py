# 휴가 기간을 넘기는 외주일 거르기
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0


def dfs(start, money):
    if start == n:
        global ans
        ans = max(ans, money)
        return

    a, b = arr[start]
    if start + a <= n:
        dfs(start + a, money + b)
    dfs(start + 1, money)


dfs(0, 0)
print(ans)