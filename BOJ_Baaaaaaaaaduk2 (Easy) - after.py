# 돌 2개 이하로 죽일 수 있는 그룹만 찾기
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def valid(i, j):
    return 0 <= i < N and 0 <= j < M

visited = [[False for _ in range(M)] for _ in range(N)]
def dfs(i, j):
    two = 1
    for d in dxy:
        a, b = i+d[0], j+d[1]
        if valid(a, b):
            if table[a][b] == 0:
                needs.add((a, b))

            elif table[a][b] == 2 and not visited[a][b]:
                visited[a][b] = True
                two += dfs(a, b)

    return two

group = []
for i in range(N):
    for j in range(M):
        if table[i][j] == 2 and not visited[i][j]:
            visited[i][j] = True
            needs = set()
            cnt = dfs(i, j)

            if len(needs) <= 2:
                group.append((needs, cnt))

ans = 0
def combi(start, pos, total):
    if len(pos) > 2:
        return

    global ans
    ans = max(ans, total)

    for i in range(start, len(group)):
        combi(i+1, pos | group[i][0], total + group[i][1])

combi(0, set(), 0)
print(ans)

