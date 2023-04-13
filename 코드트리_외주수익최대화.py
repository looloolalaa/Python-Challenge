n = int(input())
works = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if i + works[i][0] > n:
        works[i][1] = 0

temp = []
candis = []

def dfs(i):
    if i >= n:
        candis.append(sum(works[t][1] for t in temp))
        return

    for j in range(i, n):
        temp.append(j)
        dfs(j + works[j][0])
        temp.pop()

dfs(0)
# print(candis)
print(max(candis))
