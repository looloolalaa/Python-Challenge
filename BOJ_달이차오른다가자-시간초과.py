# dfs로 key가 여러개 일때 탐색
from collections import defaultdict, deque

N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]

exits = []
doors = defaultdict(list)
for i in range(N):
    for j in range(M):
        if table[i][j] == '1':
            exits.append((i, j))
        elif 'A' <= table[i][j] <= 'F':
            doors[table[i][j]].append((i, j))

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def valid(p):
    return 0<=p[0]<N and 0<=p[1]<M


result = float('inf')
def dfs(tab, dist):
    global result

    now = -1, -1
    for i in range(N):
        for j in range(M):
            if tab[i][j] == '0':
                now = i, j

    if now in exits:
        # for t in tab:
        #     print(t)
        result = min(result, dist)
        return

    dis = [[-1 for _ in range(M)] for _ in range(N)]
    que = deque([now])
    dis[now[0]][now[1]] = 0
    while que:
        n = que.popleft()
        for d in dxy:
            a = n[0]+d[0], n[1]+d[1]
            if valid(a) and dis[a[0]][a[1]] == -1 and tab[a[0]][a[1]] != '#' and not ('A' <= tab[a[0]][a[1]] <= 'F'):
                dis[a[0]][a[1]] = dis[n[0]][n[1]] + 1
                que.append(a)


    dis_exits = [dis[exi[0]][exi[1]] for exi in exits]
    # 출구로 가는 길이 하나라도 있다면
    if any(d != -1 for d in dis_exits):
        min_dis = min(dis_exits)
        for exi in exits:
            if dis[exi[0]][exi[1]] == min_dis:
                next_tab = [line[:] for line in tab]
                next_tab[now[0]][now[1]] = '.'
                next_tab[exi[0]][exi[1]] = '0'
                dfs(next_tab, dist + min_dis)
                return

    # 어느 출구로도 못 나가고

    keys = {}
    for i in range(N):
        for j in range(M):
            if 'a' <= tab[i][j] <= 'f':
                keys[(i, j)] = tab[i][j]

    can_go_keys = {}
    for k in keys:
        if dis[k[0]][k[1]] != -1:
            can_go_keys[k] = keys[k]

    # 어느 키로도 갈 수 없다면
    if not can_go_keys:
        # for t in tab:
        #     print(t)
        # print(-1)
        return

    # 키로 갈 수 있다면
    for k in can_go_keys:
        next_tab = [line[:] for line in tab]
        next_tab[now[0]][now[1]] = '.'
        next_tab[k[0]][k[1]] = '0'

        low = can_go_keys[k]
        upp = low.upper()
        if upp in doors:
            for door in doors[upp]:
                next_tab[door[0]][door[1]] = '.'

        dfs(next_tab, dist + dis[k[0]][k[1]])


dfs(table, 0)

print(-1 if result == float('inf') else result)
