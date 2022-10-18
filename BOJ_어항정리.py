# rotate & stacking

n, k = map(int, input().split())
table = [[-1 for _ in range(n)] for _ in range(n)]

fish = list(map(int, input().split()))
table[-1] = fish

def plus(p, d):
    return p[0] + d[0], p[1] + d[1]

def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n

def rotate(arr):
    return list(zip(*arr[::-1]))

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def share(height, start):
    global table

    ds = {}
    for i in range(n - height, n):
        for j in range(start, n):
            if table[i][j] == -1:
                continue

            for xy in dxy:
                new_p = plus((i, j), xy)
                if not (n - height <= new_p[0] < n and start <= new_p[1] < n) or table[new_p[0]][new_p[1]] == -1:
                    continue
                if (new_p, (i, j)) in ds:
                    continue

                d = abs(table[new_p[0]][new_p[1]] - table[i][j]) // 5
                if d > 0:
                    mi, ma = (i, j), new_p
                    if table[i][j] > table[new_p[0]][new_p[1]]:
                        mi, ma = ma, mi
                    ds[(mi, ma)] = d

    for mi, ma in ds:
        d = ds[(mi, ma)]
        table[ma[0]][ma[1]] -= d
        table[mi[0]][mi[1]] += d


    new_fish = []
    for j in range(start, n):
        for i in range(n - 1, n - height - 1, -1):
            if table[i][j] != -1:
                new_fish.append(table[i][j])

    table = [[-1 for _ in range(n)] for _ in range(n)]
    table[-1] = new_fish


count = 1
while True:
    min_fish = min(table[-1])
    for j in range(n):
        if table[n - 1][j] == min_fish:
            table[n - 1][j] += 1

    # 1
    table[n-2][1] = table[n-1][0]
    start = 1

    while True:
        height = 0
        for i in range(n-1, -1, -1):
            if table[i][start] == -1:
                break
            height += 1

        end = start
        while end < n and table[n-2][end] != -1:
            end += 1
        width = end - start
        if n - end < height:
            break

        lifted = list(map(lambda x: x[start:end], table[n-height:]))
        rotated = rotate(lifted)

        for i in range(len(rotated)):
            for j in range(len(rotated[0])):
                table[n-1-width+i][end+j] = rotated[i][j]

        start = end

    share(height, start)


    # 2
    for a in range(2):
        if a == 0:
            start = 0
            end = n//2
            width = end - start
            height = 2
        if a == 1:
            start = n//2
            end = n//2 + n//4
            width = end - start
            height = 4

        lifted = list(map(lambda x: x[start:end], table[n-(height//2):]))
        rotated = rotate(rotate(lifted))
        for i in range(len(rotated)):
            for j in range(len(rotated[0])):
                table[n-height+i][end+j] = rotated[i][j]


    share(4, end)
    diff = max(table[-1]) - min(table[-1])
    if k >= diff:
        print(count)
        break
    count += 1

# print(-1)

