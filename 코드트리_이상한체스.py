# 선풍기 돌리기
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

horses = []
for i in range(n):
    for j in range(m):
        if 1 <= table[i][j] <= 5:
            horses.append(table[i][j])

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < m


arrows = [
    [],
    [(0,), (1,), (2,), (3,)],
    [(0, 2), (1, 3)],
    [(0, 1), (1, 2), (2, 3), (3, 0)],
    [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
    [(0, 1, 2, 3)]
]


def draw(temp):
    new_table = [t[:] for t in table]

    def color(p, di):
        # (1,1) (0,2)
        now = p
        for d in di:
            nxt = now[0] + dxy[d][0], now[1] + dxy[d][1]
            while valid(nxt) and new_table[nxt[0]][nxt[1]] != 6:
                if new_table[nxt[0]][nxt[1]] == 0:
                    new_table[nxt[0]][nxt[1]] = 7
                nxt = nxt[0] + dxy[d][0], nxt[1] + dxy[d][1]

    k = 0
    for i in range(n):
        for j in range(m):
            if 1 <= new_table[i][j] <= 5:
                color((i, j), temp[k])
                k += 1

    zero_cnt = 0
    for i in range(n):
        for j in range(m):
            if new_table[i][j] == 0:
                zero_cnt += 1
    return zero_cnt


ans = int(1e9)
temp = []


def dfs(depth):
    if depth == len(horses):
        global ans
        ans = min(ans, draw(temp))
        return

    for arrow in arrows[horses[depth]]:
        temp.append(arrow)
        dfs(depth + 1)
        temp.pop()


dfs(0)
print(ans)

