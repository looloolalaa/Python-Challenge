N, M = map(int, input().split())

cards = list(map(int, input().split()))
cards.sort()
visited = [False for _ in range(N)]
temp = [-1 for _ in range(M)]
s = set()

def dfs(i):
    if i == M:
        s.add(tuple(temp))
        return

    for k in range(N):
        if not visited[k]:
            temp[i] = cards[k]
            visited[k] = True
            dfs(i+1)
            visited[k] = False

dfs(0)
result = sorted(list(s))

for r in result:
    print(*r)
