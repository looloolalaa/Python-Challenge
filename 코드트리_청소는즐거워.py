# 방향별 비율(%)

# [
#     [0,  0, 2, 0, 0],
#     [0, 10, 7, 1, 0],
#     [5,  0, 0, 0, 0],
#     [0, 10, 7, 1, 0],
#     [0,  0, 2, 0, 0],
# ]

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

orders = []
direct = [[-1 for _ in range(n)] for _ in range(n)]

dxy = [[0, -1], [1, 0], [0, 1], [-1, 0]]

def valid(p):
    return 0<=p[0]<n and 0<=p[1]<n

def init_orders():
    now = n//2, n//2
    d = 0
    dist = 0
    while valid(now):
        if d % 2 == 0:
            dist += 1

        for _ in range(dist):
            now = now[0]+dxy[d][0], now[1]+dxy[d][1]
            if not valid(now):
                break
            orders.append(now)
            direct[now[0]][now[1]] = d

        d = (d+1) % 4

def get_around(p):
    amount = {}
    dust = table[p[0]][p[1]]
    arrow = direct[p[0]][p[1]]
    d = dxy[arrow]
    # 57, (0, -1), (1, 2)

    a = p[0]+d[0], p[1]+d[1]

    front = a[0]+d[0], a[1]+d[1]
    amount[front] = int(dust * (5/100))

    # left, right
    if d[0] == 0:
        up_ten = a[0] - 1, a[1]
        down_ten = a[0] + 1, a[1]
        amount[up_ten] = int(dust * (10/100))
        amount[down_ten] = int(dust * (10 / 100))

        up_seven = p[0]-1, p[1]
        down_seven = p[0] + 1, p[1]
        amount[up_seven] = int(dust * (7 / 100))
        amount[down_seven] = int(dust * (7 / 100))

        back = p[0]-d[0], p[1]-d[1]
        up_one = back[0]-1, back[1]
        down_one = back[0] + 1, back[1]
        amount[up_one] = int(dust * (1 / 100))
        amount[down_one] = int(dust * (1 / 100))

        up_two = up_seven[0]-1, up_seven[1]
        down_two = down_seven[0]+1, down_seven[1]
        amount[up_two] = int(dust * (2 / 100))
        amount[down_two] = int(dust * (2 / 100))

    else:
        up_ten = a[0], a[1]-1
        down_ten = a[0], a[1]+1
        amount[up_ten] = int(dust * (10 / 100))
        amount[down_ten] = int(dust * (10 / 100))

        up_seven = p[0], p[1]-1
        down_seven = p[0], p[1]+1
        amount[up_seven] = int(dust * (7 / 100))
        amount[down_seven] = int(dust * (7 / 100))

        back = p[0] - d[0], p[1] - d[1]
        up_one = back[0], back[1]-1
        down_one = back[0], back[1]+1
        amount[up_one] = int(dust * (1 / 100))
        amount[down_one] = int(dust * (1 / 100))

        up_two = up_seven[0], up_seven[1]-1
        down_two = down_seven[0], down_seven[1]+1
        amount[up_two] = int(dust * (2 / 100))
        amount[down_two] = int(dust * (2 / 100))


    a_dust = dust - sum(amount[near] for near in amount)
    amount[a] = a_dust

    return amount

result = 0


init_orders()
for i, j in orders:
    around = get_around((i, j))
    for p in around:
        if valid(p):
            table[p[0]][p[1]] += around[p]
        else:
            result += around[p]
    table[i][j] = 0


# for t in table:
#     print(t)
print(result)