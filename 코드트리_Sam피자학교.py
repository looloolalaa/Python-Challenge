# 말아 올리기
# 규칙성이 있긴 하지만 ..
n, k = map(int, input().split())
temp = list(map(int, input().split()))

# n = 12
# temp = [i+1 for i in range(n)]

table = [[0 for _ in range(n)] for _ in range(n)]
table[n - 1] = temp


def plus():
    bread = table[n - 1]
    mini = min(bread)
    for j in range(n):
        if table[n - 1][j] == mini:
            table[n - 1][j] += 1


def get_rect():
    start_j, end_j = -1, -1
    for j in range(n):
        if table[n - 1][j] != 0:
            start_j = j
            break
    for j in range(n - 1, -1, -1):
        if table[n - 2][j] != 0:
            end_j = j
            break

    start_i = -1
    for i in range(n):
        if table[i][start_j] != 0:
            start_i = i
            break

    return start_i, start_j, end_j


def rotated(arr):
    return list(zip(*arr[::-1]))


def up():
    start_i, start_j, end_j = get_rect()
    width, height = n - start_i, end_j - start_j + 1
    if width > n - end_j - 1:
        return -1

    rect = [[0 for _ in range(height)] for _ in range(width)]
    for i in range(start_i, n):
        for j in range(start_j, end_j + 1):
            rect[i - start_i][j - start_j] = table[i][j]
            table[i][j] = 0

    rolled = rotated(rect)
    rolled_width, rolled_height = len(rolled[0]), len(rolled)

    new_i, new_j = n - 2, end_j + 1

    for i in range(new_i, new_i - rolled_height, -1):
        for j in range(new_j, new_j + rolled_width):
            table[i][j] = rolled[i - new_i + rolled_height - 1][j - new_j]


def roll():
    table[n - 2][1] = table[n - 1][0]
    table[n - 1][0] = 0

    while True:
        if up() == -1:
            break


dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


def press():
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] != 0:
                for d in dxy:
                    a = i + d[0], j + d[1]
                    if valid(a) and table[a[0]][a[1]] != 0:
                        x = table[i][j]
                        y = table[a[0]][a[1]]
                        z = abs(x - y) // 5
                        big, small = (a, (i, j)) if table[a[0]][a[1]] > table[i][j] else ((i, j), a)
                        temp[big[0]][big[1]] -= z
                        temp[small[0]][small[1]] += z

    for i in range(n):
        for j in range(n):
            table[i][j] += temp[i][j] // 2


def spread():
    temp = []
    for j in range(n):
        for i in range(n - 1, -1, -1):
            if table[i][j] != 0:
                temp.append(table[i][j])
    for i in range(n):
        for j in range(n):
            table[i][j] = 0
    table[n - 1] = temp


def up2():
    temp = [0 for _ in range(n // 2)]
    for j in range(n // 2):
        temp[j] = table[n - 1][j]
        table[n - 1][j] = 0
    for j in range(n // 2):
        table[n - 2][n - 1 - j] = temp[j]

    temp = [[0 for _ in range(n // 4)] for _ in range(2)]
    for i in range(n - 2, n):
        for j in range(n // 2, (n // 4) * 3):
            temp[i - (n - 2)][j - n // 2] = table[i][j]
            table[i][j] = 0

    for _ in range(2):
        temp = rotated(temp)

    for i in range(n - 4, n - 2):
        for j in range((n // 4) * 3, n):
            table[i][j] = temp[i - (n - 4)][j - ((n // 4) * 3)]


def diff():
    mini, maxi = min(table[n - 1]), max(table[n - 1])
    return maxi - mini


def simulate():
    plus()
    roll()
    press()
    spread()
    up2()
    press()
    spread()


# for t in table:
#     print(t)

time = 0
while diff() > k:
    simulate()
    time += 1

print(time)