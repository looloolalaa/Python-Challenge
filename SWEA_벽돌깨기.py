# product
from collections import deque

test_results = []
t = int(input())
for _ in range(t):

    n, w, h = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(h)]

    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]


    def plus(p, d):
        return (p[0] + d[0], p[1] + d[1])


    def remain_count(tab, order):
        # (2,2,6)
        def valid(p):
            return 0 <= p[0] < h and 0 <= p[1] < w

        def bomb_BFS(j):
            top = (0, j)
            while valid(top) and tab[top[0]][top[1]] == 0:
                top = plus(top, dxy[1])

            que = deque([top])
            while que:
                now = que.popleft()
                if not valid(now) or tab[now[0]][now[1]] == 0:
                    continue

                num = tab[now[0]][now[1]]
                tab[now[0]][now[1]] = 0
                for d in dxy:
                    center = now
                    for _ in range(num - 1):
                        center = plus(center, d)
                        que.append(center)

        def bomb_DFS(j):
            def dfs(p):
                if not valid(p) or tab[p[0]][p[1]] == 0:
                    return

                num = tab[p[0]][p[1]]
                tab[p[0]][p[1]] = 0
                for d in dxy:
                    center = p
                    for _ in range(num - 1):
                        center = plus(center, d)
                        dfs(center)

            top = (0, j)
            while valid(top) and tab[top[0]][top[1]] == 0:
                top = plus(top, dxy[1])

            dfs(top)


        def down():
            for j in range(w):
                rem = []
                for i in range(h):
                    if tab[i][j] != 0:
                        rem.append(tab[i][j])

                i = h - 1
                while rem:
                    tab[i][j] = rem.pop()
                    i -= 1
                while valid((i, j)):
                    tab[i][j] = 0
                    i -= 1

        def remain():
            count = 0
            for i in range(h):
                for j in range(w):
                    if tab[i][j] != 0:
                        count += 1
            return count

        for o in order:
            bomb_DFS(o)
            down()

        return remain()


    candis = []
    cards = [j for j in range(w)]
    temp = [0 for _ in range(n)]


    def dfs(i):
        if i == n:
            candis.append(temp[:])
            return
        for j in range(w):
            temp[i] = cards[j]
            dfs(i+1)


    dfs(0)
    results = []
    for c in candis:
        new_table = [line[:] for line in table]
        rc = remain_count(new_table, c)
        results.append(rc)
        if rc == 0:
            break

    test_results.append(min(results))

for i in range(len(test_results)):
    print('#{} {}'.format(i+1, test_results[i]))