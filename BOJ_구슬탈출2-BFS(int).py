# int(좌표) 들고 다니기 + visited
# table 하나도 수정 X
from collections import deque

n, m = map(int, input().split())
table = [list(input()) for _ in range(n)]

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def plus(p, d):
    return p[0] + d[0], p[1] + d[1]


def minus(p, d):
    return p[0] - d[0], p[1] - d[1]


def go(red, blue, d):
    def move(p):
        m_p = plus(p, d)
        while table[m_p[0]][m_p[1]] != '#':
            if table[m_p[0]][m_p[1]] == 'O':
                return m_p
            m_p = plus(m_p, d)
        m_p = minus(m_p, d)
        return m_p

    if (
            (d == (0, 1) and red[1] < blue[1]) or
            (d == (1, 0) and red[0] < blue[0]) or
            (d == (0, -1) and red[1] > blue[1]) or
            (d == (-1, 0) and red[0] > blue[0])
    ):

        new_blue = move(blue)
        new_red = move(red)
        if new_blue == new_red and table[new_blue[0]][new_blue[1]] != 'O':
            new_red = minus(new_red, d)
        return new_red, new_blue

    new_red = move(red)
    new_blue = move(blue)
    if new_blue == new_red and table[new_blue[0]][new_blue[1]] != 'O':
        new_blue = minus(new_blue, d)
    return new_red, new_blue



def check(red, blue):
    red_out = True if table[red[0]][red[1]] == 'O' else False
    blue_out = True if table[blue[0]][blue[1]] == 'O' else False

    if blue_out:
        return 0
    elif red_out:
        return 1
    else:
        return 2


def can_go(red, blue, d):
    next_red = plus(red, d)
    next_blue = plus(blue, d)
    next_red_value = table[next_red[0]][next_red[1]]
    next_blue_value = table[next_blue[0]][next_blue[1]]

    if next_red_value != '#':
        return True
    if next_blue_value != '#':
        return True

    return False


red_start, blue_start = (-1, -1), (-1, -1)
for i in range(n):
    for j in range(m):
        if table[i][j] == 'R':
            red_start = (i, j)
        if table[i][j] == 'B':
            blue_start = (i, j)


min_depth = float('inf')

visited = set()
que = deque([(red_start, blue_start, 0)])
while que:
    red, blue, depth = que.popleft()
    if (red, blue) in visited:
        continue
    visited.add((red, blue))

    if depth > 10:
        continue

    c = check(red, blue)
    if c == 0:
        continue
    if c == 1 and min_depth > depth:
        min_depth = depth
        continue

    for d in dxy:
        if can_go(red, blue, d):
            new_red, new_blue = go(red, blue, d)
            que.append((new_red, new_blue, depth + 1))


print(min_depth if min_depth != float('inf') else -1)




