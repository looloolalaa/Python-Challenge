# 야구 룰
from itertools import permutations
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def total(order):
    return sum(score(order, a) for a in arr)

def score(order, a):
    base = [0, 0, 0]
    out = 0
    sco = 0
    while out < 3:
        player = order.popleft()
        order.append(player)
        if a[player] == 0:
            out += 1
            continue

        d = a[player]
        if d == 1:
            sco += base[2]
            base = [1, base[0], base[1]]
        elif d == 2:
            sco += base[2] + base[1]
            base = [0, 1, base[0]]
        elif d == 3:
            sco += base[2] + base[1] + base[0]
            base = [0, 0, 1]
        elif d == 4:
            sco += base[2] + base[1] + base[0] + 1
            base = [0, 0, 0]

    return sco

ans = 0
for p in permutations([i for i in range(1, 9)], 8):
    order = list(p)
    order.insert(3, 0)
    order = deque(order)
    ans = max(ans, total(order))

print(ans)
