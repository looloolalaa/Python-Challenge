from collections import deque

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

shark = (-1, -1)
for i in range(n):
    for j in range(n):
        if table[i][j] == 9:
            shark = (i, j)

size = 2
level = 0

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def plus(p, d):
    return p[0] + d[0], p[1] + d[1]


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


def near_fish(pos, size):
    min_fish = float('inf'), (-1, -1)

    visited = set()
    que = deque([(0, pos)])
    while que:
        d, p = que.popleft()
        if p in visited or not valid(p) or d > min_fish[0]:
            continue
        visited.add(p)

        if table[p[0]][p[1]] > size and table[p[0]][p[1]] != 9:
            continue

        if 0 < table[p[0]][p[1]] < size:
            if table[p[0]][p[1]] != 9 and min_fish[0] >= d:
                min_fish = min(min_fish, (d, p))

        for xy in dxy:
            que.append((d+1, plus(p, xy)))

    return min_fish


move = 0
fish = near_fish(shark, size)
while fish != (float('inf'), (-1, -1)):
    dis, fish_p = fish

    # eat
    if table[shark[0]][shark[1]] == 9:
        table[shark[0]][shark[1]] = 0
    table[fish_p[0]][fish_p[1]] = 9
    shark = (fish_p[0], fish_p[1])
    move += dis

    level += 1
    if level == size:
        level = 0
        size += 1

    fish = near_fish(shark, size)


print(move)
