# 2차원배열 벽에서 반사되며 이동
from collections import defaultdict

n, m, k = map(int, input().split())
pos = [];
s = [];
d = [];
b = []
for _ in range(k):
    q, w, e, r, t = map(int, input().split())
    pos.append((q - 1, w - 1))
    s.append(e)
    d.append(r)
    b.append(t)


def next_pos_and_dir(p, s, d):
    # up down
    if d <= 2:
        inplace = 2 * (n - 1)
        move = s % inplace
        if d == 2:
            new_i = p[0] + move
            if new_i < n - 1:
                return ((new_i, p[1]), 2)
            else:
                return next_pos_and_dir((n - 1, p[1]), move - ((n - 1) - p[0]), 1)

        elif d == 1:
            new_i = p[0] - move
            if new_i > 0:
                return ((new_i, p[1]), 1)
            else:
                return next_pos_and_dir((0, p[1]), move - p[0], 2)

    # left right
    elif d > 2:
        inplace = 2 * (m - 1)
        move = s % inplace
        if d == 3:
            new_j = p[1] + move
            if new_j < m - 1:
                return ((p[0], new_j), 3)
            else:
                return next_pos_and_dir((p[0], m - 1), move - ((m - 1) - p[1]), 4)

        elif d == 4:
            new_j = p[1] - move
            if new_j > 0:
                return ((p[0], new_j), 4)
            else:
                return next_pos_and_dir((p[0], 0), move - p[1], 3)

    return -1


alive = set(i for i in range(k))


def target(j):
    targets = []
    for a in alive:
        if pos[a][1] == j:
            targets.append(a)

    if not targets:
        return -1
    return min(targets, key=lambda x: pos[x][0])


def go():
    for a in alive:
        new_p, new_d = next_pos_and_dir(pos[a], s[a], d[a])
        pos[a] = new_p
        d[a] = new_d


def die():
    book = defaultdict(list)
    for a in alive:
        book[pos[a]].append(a)

    for p, aa in book.items():
        if len(aa) >= 2:
            king = max(aa, key=lambda x: b[x])
            dead = [a for a in aa if a != king]

            for a in dead:
                alive.remove(a)


ans = 0
for j in range(m):
    t = target(j)
    if t >= 0:
        alive.remove(t)
        ans += b[t]
    go()
    die()

print(ans)