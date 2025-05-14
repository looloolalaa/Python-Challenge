# 사람으로 카시궁 가리기
from collections import deque

N, M = map(int, input().split())
sr, sc, er, ec = map(int, input().split())
warriors = [[[] for _ in range(N)] for _ in range(N)]
wa_pos = {}
wa = list(map(int, input().split()))
for m in range(M):
    p = wa[2 * m], wa[2 * m + 1]
    warriors[p[0]][p[1]].append(m + 1)
    wa_pos[m + 1] = (p[0], p[1])

table = [list(map(int, input().split())) for _ in range(N)]

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def valid(p):
    return 0 <= p[0] < N and 0 <= p[1] < N


def see():
    # up
    caught1 = []
    saw1 = [[0 for _ in range(N)] for _ in range(N)]
    width = 1
    for i in range(sr - 1, -1, -1):
        for j in range(sc - width, sc + width + 1):
            if not valid((i, j)) or saw1[i][j] == 2:
                continue

            saw1[i][j] = 1
            if not warriors[i][j]:
                continue

            caught1 += warriors[i][j]
            for x in range(i):
                saw1[x][j] = 2

            if j == sc:
                continue

            if j < sc:
                k = i
                for y in range(j - 1, -1, -1):
                    for x in range(k):
                        saw1[x][y] = 2
                    k -= 1
            elif sc < j:
                k = i
                for y in range(j + 1, N):
                    for x in range(k):
                        saw1[x][y] = 2
                    k -= 1

        width += 1

    # down
    caught2 = []
    saw2 = [[0 for _ in range(N)] for _ in range(N)]
    width = 1
    for i in range(sr + 1, N):
        for j in range(sc - width, sc + width + 1):
            if not valid((i, j)) or saw2[i][j] == 2:
                continue

            saw2[i][j] = 1
            if not warriors[i][j]:
                continue

            caught2 += warriors[i][j]
            for x in range(i + 1, N):
                saw2[x][j] = 2

            if j == sc:
                continue

            if j < sc:
                k = N - i
                for y in range(j - 1, -1, -1):
                    for x in range(N - 1, N - k, -1):
                        saw2[x][y] = 2
                    k -= 1
            elif sc < j:
                k = N - i
                for y in range(j + 1, N):
                    for x in range(N - 1, N - k, -1):
                        saw2[x][y] = 2
                    k -= 1

        width += 1

    # left
    caught3 = []
    saw3 = [[0 for _ in range(N)] for _ in range(N)]
    width = 1
    for j in range(sc - 1, -1, -1):
        for i in range(sr - width, sr + width + 1):
            if not valid((i, j)) or saw3[i][j] == 2:
                continue

            saw3[i][j] = 1
            if not warriors[i][j]:
                continue

            caught3 += warriors[i][j]
            for y in range(j - 1, -1, -1):
                saw3[i][y] = 2

            if i == sr:
                continue

            if i < sr:
                k = j
                for x in range(i - 1, -1, -1):
                    for y in range(k):
                        saw3[x][y] = 2
                    k -= 1
            elif sr < i:
                k = j
                for x in range(i + 1, N):
                    for y in range(k):
                        saw3[x][y] = 2
                    k -= 1

        width += 1

    # right
    caught4 = []
    saw4 = [[0 for _ in range(N)] for _ in range(N)]
    width = 1
    for j in range(sc + 1, N):
        for i in range(sr - width, sr + width + 1):
            if not valid((i, j)) or saw4[i][j] == 2:
                continue

            saw4[i][j] = 1
            if not warriors[i][j]:
                continue

            caught4 += warriors[i][j]
            for y in range(j + 1, N):
                saw4[i][y] = 2

            if i == sr:
                continue

            if i < sr:
                k = N - j
                for x in range(i - 1, -1, -1):
                    for y in range(N - 1, N - k, -1):
                        saw4[x][y] = 2
                    k -= 1
            elif sr < i:
                k = N - j
                for x in range(i + 1, N):
                    for y in range(N - 1, N - k, -1):
                        saw4[x][y] = 2
                    k -= 1

        width += 1

    maxi, max_idx = -1, -1
    candi = [caught1, caught2, caught3, caught4]
    for i in range(4):
        if maxi < len(candi[i]):
            maxi = len(candi[i])
            max_idx = i

    res = -1, -1
    if max_idx == 0:
        res = caught1, saw1
    elif max_idx == 1:
        res = caught2, saw2
    elif max_idx == 2:
        res = caught3, saw3
    elif max_idx == 3:
        res = caught4, saw4

    return res


dist = [[-1 for _ in range(N)] for _ in range(N)]
dist[er][ec] = 0
que = deque([(er, ec)])
while que:
    now = que.popleft()
    for d in dxy:
        a = now[0] + d[0], now[1] + d[1]
        if valid(a) and dist[a[0]][a[1]] == -1 and table[a[0]][a[1]] == 0:
            dist[a[0]][a[1]] = dist[now[0]][now[1]] + 1
            que.append(a)

if dist[sr][sc] == -1:
    print(-1)
    exit(0)


def next_pos():
    res = -1
    mini = int(1e9)
    for d in dxy:
        a = sr + d[0], sc + d[1]
        if valid(a) and dist[a[0]][a[1]] != -1 and dist[a[0]][a[1]] < mini:
            mini = dist[a[0]][a[1]]
            res = d
    return (sr + res[0], sc + res[1])


# turn = 1
while True:
    # 1)
    sr, sc = next_pos()
    if (sr, sc) == (er, ec):
        print(0)
        exit(0)

    for w in warriors[sr][sc]:
        wa_pos.pop(w)
    warriors[sr][sc] = []

    # 2)
    stone, saw = see()

    dist_m = [[-1 for _ in range(N)] for _ in range(N)]
    dist_m[sr][sc] = 0
    que = deque([(sr, sc)])
    while que:
        now = que.popleft()
        for d in dxy:
            a = now[0] + d[0], now[1] + d[1]
            if valid(a) and dist_m[a[0]][a[1]] == -1:
                dist_m[a[0]][a[1]] = dist_m[now[0]][now[1]] + 1
                que.append(a)


    def next_wa_pos(w, num):
        p = wa_pos[w]
        res = -1
        mini = int(1e9)
        direc = dxy if num == 0 else [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for d in direc + [[0, 0]]:
            a = p[0] + d[0], p[1] + d[1]
            if valid(a) and dist_m[a[0]][a[1]] < mini and saw[a[0]][a[1]] != 1:
                mini = dist_m[a[0]][a[1]]
                res = d
        return (p[0] + res[0], p[1] + res[1])


    # 3)
    wa_move = 0
    for w in wa_pos:
        if w in stone:
            continue

        for num in range(2):
            p = wa_pos[w]
            np = next_wa_pos(w, num)
            warriors[p[0]][p[1]].remove(w)
            warriors[np[0]][np[1]].append(w)
            wa_pos[w] = np
            wa_move += abs(np[0] - p[0]) + abs(np[1] - p[1])

    # 4)
    attack = len(warriors[sr][sc])
    for w in warriors[sr][sc]:
        wa_pos.pop(w)
    warriors[sr][sc] = []

    # print(turn)
    # print(sr, sc)
    # for w in warriors:
    #     print(w)
    # print(stone)
    # for s in saw:
    #     print(s)
    # print()
    # for di in dist_m:
    #     print(di)
    # turn += 1
    print(wa_move, len(stone), attack)

