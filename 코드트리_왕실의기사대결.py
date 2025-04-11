# 사각형 밀기 => 연쇄 밀림 dfs
# (사각형 트리 중복 조심)
# a~b c~d 범위 겹침 조건
L, N, Q = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(L)]
people = [list(map(int, input().split())) for _ in range(N)]
initial_hp = [person[4] for person in people]
for person in people:
    person[0] -= 1
    person[1] -= 1
commands = [list(map(int, input().split())) for _ in range(Q)]
for com in commands:
    com[0] -= 1

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]
def valid(p):
    return 0 <= p[0] < L and 0 <= p[1] < L


tree = set()
can_push_all = True
def dfs(num, di):
    global can_push_all
    r, c, h, w, k = people[num]

    if di % 2 == 0:
        topOrBottom = r - 1 if di == 0 else r + h
        j_start, j_end = c, c+w-1
        for j in range(j_start, j_end+1):
            if not valid((topOrBottom, j)) or table[topOrBottom][j] == 2:
                can_push_all = False
                return

        tree.add(num)
        for n in range(N):
            if n != num and people[n][4] > 0:
                a, b, c, d, _ = people[n]
                line = a if di == 2 else a + c - 1
                s, e = b, b + d - 1
                if line == topOrBottom and j_start <= e and s <= j_end:
                    dfs(n, di)

    elif di % 2 == 1:
        leftOrRight = c + w if di == 1 else c - 1
        i_start, i_end = r, r + h-1
        for i in range(i_start, i_end+1):
            if not valid((i, leftOrRight)) or table[i][leftOrRight] == 2:
                can_push_all = False
                return

        tree.add(num)
        for n in range(N):
            if n != num and people[n][4] > 0:
                a, b, c, d, _ = people[n]
                line = b if di == 1 else b + d - 1
                s, e = a, a + c - 1
                if line == leftOrRight and i_start <= e and s <= i_end:
                    dfs(n, di)


for num, di in commands:
    if people[num][4] <= 0:
        continue

    can_push_all = True
    tree = set()
    dfs(num, di)
    if can_push_all:
        for n in tree:
            people[n][0] += dxy[di][0]
            people[n][1] += dxy[di][1]

            if n != num:
                r, c, h, w, _ = people[n]
                damage = 0
                for i in range(r, r + h):
                    for j in range(c, c + w):
                        if table[i][j] == 1:
                            damage += 1
                people[n][4] -= damage


ans = 0
for n in range(N):
    if people[n][4] > 0:
        ans += initial_hp[n] - people[n][4]
print(ans)