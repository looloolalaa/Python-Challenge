# 둥근 격자
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
moves = [list(map(int, input().split())) for _ in range(m)]

pills = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

dxy = {1: [0, 1], 2: [-1, 1], 3: [-1, 0], 4: [-1, -1], 5: [0, -1], 6: [1, -1], 7: [1, 0], 8: [1, 1]}


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


def move(arrow, dist):
    plus = list(map(lambda x: x * dist, dxy[arrow]))
    for i in range(len(pills)):
        pill = pills[i]
        new_pill = [pill[0] + plus[0], pill[1] + plus[1]]
        if new_pill[0] >= n:
            new_pill[0] = new_pill[0] % n
        elif new_pill[0] < 0:
            while new_pill[0] < 0:
                new_pill[0] = new_pill[0] + n

        if new_pill[1] >= n:
            new_pill[1] = new_pill[1] % n
        elif new_pill[1] < 0:
            while new_pill[1] < 0:
                new_pill[1] = new_pill[1] + n

        pills[i] = new_pill


def grow():
    for pill in pills:
        table[pill[0]][pill[1]] += 1


def grow_more():
    counter = [0 for _ in range(len(pills))]
    diago = [2, 4, 6, 8]
    for i in range(len(pills)):
        pill = pills[i]
        c = 0
        for d in diago:
            a = pill[0] + dxy[d][0], pill[1] + dxy[d][1]
            if valid(a) and table[a[0]][a[1]] >= 1:
                c += 1
        counter[i] = c

    for i in range(len(pills)):
        pill = pills[i]
        table[pill[0]][pill[1]] += counter[i]


def cut():
    global pills
    new_pills = []
    for i in range(n):
        for j in range(n):
            if [i, j] in pills:
                continue

            if table[i][j] >= 2:
                table[i][j] -= 2
                new_pills.append([i, j])

    pills.clear()
    pills = new_pills


def total():
    to = 0
    for i in range(n):
        for j in range(n):
            to += table[i][j]
    return to


for i in range(m):
    d, p = moves[i]
    move(d, p)
    grow()
    grow_more()
    cut()

print(total())
