# dfs - 3명이 한 칸씩 이동
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

friends = []
for _ in range(m):
    i, j = map(int, input().split())
    friends.append((i - 1, j - 1))

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


ans = 0
def dfs(depth, total):
    if depth == 3 * m:
        global ans
        ans = max(ans, total)
        return

    friend = friends[depth % m]
    for d in dxy:
        a = friend[0] + d[0], friend[1] + d[1]
        if valid(a):
            friends[depth % m] = a
            amount = table[a[0]][a[1]]
            table[a[0]][a[1]] = 0

            dfs(depth + 1, total + amount)

            table[a[0]][a[1]] = amount
            friends[depth % m] = friend


s = 0
for friend in friends:
    s += table[friend[0]][friend[1]]
    table[friend[0]][friend[1]] = 0

dfs(0, s)
print(ans)
