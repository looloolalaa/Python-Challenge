# 3차원 면으로 graph 만들기
# 시간이 필요한 BFS
from collections import defaultdict, deque

N, M, F = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

cube = [[9 for _ in range(3 * M)] for _ in range(3 * M)]


def rotated(arr):
    return list(zip(*arr[::-1]))


# 동
face = [list(map(int, input().split())) for _ in range(M)]
for _ in range(3):
    face = rotated(face)
for i in range(M, 2 * M):
    for j in range(2 * M, 3 * M):
        cube[i][j] = face[i - M][j - 2 * M]

# 서
face = [list(map(int, input().split())) for _ in range(M)]
for _ in range(1):
    face = rotated(face)
for i in range(M, 2 * M):
    for j in range(M):
        cube[i][j] = face[i - M][j]

# 남
face = [list(map(int, input().split())) for _ in range(M)]
for _ in range(0):
    face = rotated(face)
for i in range(2 * M, 3 * M):
    for j in range(M, 2 * M):
        cube[i][j] = face[i - 2 * M][j - M]

# 북
face = [list(map(int, input().split())) for _ in range(M)]
for _ in range(2):
    face = rotated(face)
for i in range(M):
    for j in range(M, 2 * M):
        cube[i][j] = face[i][j - M]

# 윗
face = [list(map(int, input().split())) for _ in range(M)]
for _ in range(0):
    face = rotated(face)
for i in range(M, 2 * M):
    for j in range(M, 2 * M):
        cube[i][j] = face[i - M][j - M]

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def valid1(p):
    return 0 <= p[0] < N and 0 <= p[1] < N


def valid2(p):
    return 0 <= p[0] < 3 * M and 0 <= p[1] < 3 * M


table_id = [[0 for _ in range(N)] for _ in range(N)]
cube_id = [[0 for _ in range(3 * M)] for _ in range(3 * M)]
cnt = 1
for i in range(N):
    for j in range(N):
        table_id[i][j] = cnt
        cnt += 1
cnt = -1
for i in range(3 * M):
    for j in range(3 * M):
        if cube[i][j] != 9:
            cube_id[i][j] = cnt
            cnt -= 1

graph = defaultdict(set)
for i in range(N):
    for j in range(N):
        if table[i][j] in (0, 4):
            for d in dxy:
                a = i + d[0], j + d[1]
                if valid1(a) and table[a[0]][a[1]] in (0, 4):
                    x, y = table_id[i][j], table_id[a[0]][a[1]]
                    graph[x].add(y)
                    graph[y].add(x)

for i in range(3 * M):
    for j in range(3 * M):
        if cube[i][j] in (0, 2):
            for d in dxy:
                a = i + d[0], j + d[1]
                if valid2(a) and cube[a[0]][a[1]] in (0, 2):
                    x, y = cube_id[i][j], cube_id[a[0]][a[1]]
                    graph[x].add(y)
                    graph[y].add(x)


def try_insert(a, b):
    if cube[a[0]][a[1]] == 0 and cube[b[0]][b[1]] == 0:
        x, y = cube_id[a[0]][a[1]], cube_id[b[0]][b[1]]
        graph[x].add(y)
        graph[y].add(x)


p = 0
for _ in range(M):
    a, b = (p, M), (M, p)
    try_insert(a, b)
    p += 1
p = 0
for _ in range(M):
    a, b = (p, 2 * M - 1), (M, 3 * M - 1 - p)
    try_insert(a, b)
    p += 1
p = 0
for _ in range(M):
    a, b = (2 * M - 1, p), (p, M)
    try_insert(a, b)
    p += 1
p = 0
for _ in range(M):
    a, b = (2 * M + p, 2 * M - 1), (2 * M - 1, 2 * M + p)
    try_insert(a, b)
    p += 1

s = -1, -1
for i in range(N):
    for j in range(N):
        if table[i][j] == 3:
            s = i, j
            break
    if s != (-1, -1):
        break


def try_insert2(a, b):
    if cube[a[0]][a[1]] == 0 and table[b[0]][b[1]] == 0:
        x, y = cube_id[a[0]][a[1]], table_id[b[0]][b[1]]
        graph[x].add(y)
        graph[y].add(x)


p = 0
for _ in range(M):
    a, b = (0, M + p), (s[0] - 1, s[1] + p)
    try_insert2(a, b)
    p += 1
p = 0
for _ in range(M):
    a, b = (M + p, 3 * M - 1), (s[0] + p, s[1] + M)
    try_insert2(a, b)
    p += 1
p = 0
for _ in range(M):
    a, b = (M + p, 0), (s[0] + p, s[1] - 1)
    try_insert2(a, b)
    p += 1
p = 0
for _ in range(M):
    a, b = (3 * M - 1, M + p), (s[0] + M, s[1] + p)
    try_insert2(a, b)
    p += 1

start_id = -1
for i in range(3 * M):
    for j in range(3 * M):
        if cube[i][j] == 2:
            start_id = cube_id[i][j]
end_id = -1
for i in range(N):
    for j in range(N):
        if table[i][j] == 4:
            end_id = table_id[i][j]

ff = [list(map(int, input().split())) for _ in range(F)]
cant_go = set()
for f in ff:
    cant_go.add(table_id[f[0]][f[1]])

dist = {start_id: 0}
que = deque([start_id])
time = 1
while True:
    # virus move
    for i in range(F):
        if time % ff[i][3] == 0:
            f = ff[i]
            next_pos = f[0] + dxy[f[2]][0], f[1] + dxy[f[2]][1]
            if not valid1(next_pos) or table[next_pos[0]][next_pos[1]] != 0:
                continue

            target_id = table_id[next_pos[0]][next_pos[1]]
            cant_go.add(target_id)
            ff[i][0], ff[i][1] = next_pos[0], next_pos[1]

    # my move
    next_que = deque()
    while que:
        node = que.popleft()
        for a in graph[node]:
            if a not in dist and a not in cant_go:
                dist[a] = time
                next_que.append(a)

    if not next_que:
        break
    que = next_que
    time += 1

print(dist[end_id] if end_id in dist else -1)
