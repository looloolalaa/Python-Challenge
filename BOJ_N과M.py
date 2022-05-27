N, M = map(int, input().split())

cards = [i+1 for i in range(N)]
visited = [False for _ in range(N)]
result = [0 for _ in range(M)]


def dfs(i):
    if i == len(result):
        for r in result:
            print(r, end=' ')
        print()
        return
    for j in range(N):
        if not visited[j]:
            result[i] = cards[j]
            visited[j] = True
            dfs(i+1)
            visited[j] = False


dfs(0)