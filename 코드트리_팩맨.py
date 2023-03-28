# 상상상 상상좌 ..
monsters = [[[] for _ in range(4)] for _ in range(4)]
eggs = [[[] for _ in range(4)] for _ in range(4)]
ghost = [[0 for _ in range(4)] for _ in range(4)]

m, t = map(int, input().split())
r, c = map(int, input().split())
man = r - 1, c - 1
for _ in range(m):
    r, c, d = map(int, input().split())
    monsters[r - 1][c - 1].append(d)


def try_copy():
    for i in range(4):
        for j in range(4):
            if monsters[i][j]:
                eggs[i][j] += monsters[i][j][:]


dxy = {1: [-1, 0], 2: [-1, -1], 3: [0, -1], 4: [1, -1], 5: [1, 0], 6: [1, 1], 7: [0, 1], 8: [-1, 1]}


def can_go(p):
    return 0 <= p[0] < 4 and 0 <= p[1] < 4 and p != man and ghost[p[0]][p[1]] == 0


def next_pos(p, d):
    next_p = p[0] + dxy[d][0], p[1] + dxy[d][1]
    for _ in range(8):
        if can_go(next_p):
            return next_p, d
        else:
            d = (d + 1) if d != 8 else 1
            next_p = p[0] + dxy[d][0], p[1] + dxy[d][1]
    return p, d


def go_monsters():
    global monsters
    new_monsters = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if monsters[i][j]:
                now = i, j
                mons = monsters[i][j][:]  # [5, 7]
                for d in mons:
                    new_p, new_d = next_pos(now, d)
                    new_monsters[new_p[0]][new_p[1]].append(new_d)
    monsters = new_monsters


def valid(p):
    return 0 <= p[0] < 4 and 0 <= p[1] < 4


def eating_count(temp):
    visited = [[False for _ in range(4)] for _ in range(4)]
    move = man
    count = 0
    for d in temp:
        next_move = move[0] + dxy[d][0], move[1] + dxy[d][1]
        if valid(next_move):
            if not visited[next_move[0]][next_move[1]]:
                move = next_move
                visited[move[0]][move[1]] = True
                count += len(monsters[move[0]][move[1]])
        else:
            return -1

    return count


max_eat = -1


def go_man():
    result = [-1, -1, -1]
    temp = [-1, -1, -1]
    arrows = [1, 3, 5, 7]

    global max_eat
    max_eat = -1

    def dfs(j):
        if j == 3:
            global max_eat
            eat = eating_count(temp)
            if eat < 0:
                return
            elif max_eat < eat:
                for i in range(3):
                    result[i] = temp[i]
                max_eat = eat
            return
        for i in range(4):
            temp[j] = arrows[i]
            dfs(j + 1)

    dfs(0)
    global man
    for d in result:
        new_man = man[0] + dxy[d][0], man[1] + dxy[d][1]
        if valid(new_man):
            man = new_man
            if monsters[man[0]][man[1]]:
                monsters[man[0]][man[1]] = []
                ghost[man[0]][man[1]] = 3


def delete_ghost():
    for i in range(4):
        for j in range(4):
            if ghost[i][j] > 0:
                ghost[i][j] -= 1


def complete_copy():
    for i in range(4):
        for j in range(4):
            if eggs[i][j]:
                monsters[i][j] += eggs[i][j]
                eggs[i][j] = []


def simulate():
    try_copy()
    go_monsters()
    go_man()
    delete_ghost()
    complete_copy()


# simulate()

for _ in range(t):
    simulate()

# for m in monsters:
#     print(m)
# print()
# for e in eggs:
#     print(e)
# print()
# for g in ghost:
#     print(g)
# print()


count = 0
for i in range(4):
    for j in range(4):
        count += len(monsters[i][j])
print(count)