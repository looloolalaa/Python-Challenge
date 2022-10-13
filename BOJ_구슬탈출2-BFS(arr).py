# table 을 계속 수정하면서 인자로 들고 다니는 것은 매우 비효율적
from collections import deque

n, m = map(int, input().split())
table = [list(input()) for _ in range(n)]

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def plus(p, d):
    return p[0] + d[0], p[1] + d[1]


def minus(p, d):
    return p[0] - d[0], p[1] - d[1]


def go(tab, d):
    first, second = (-1, -1), (-1, -1)
    for i in range(n):
        for j in range(m):
            if tab[i][j] == 'R':
                first = (i, j)
            if tab[i][j] == 'B':
                second = (i, j)


    if d == (0, 1) and first[1] < second[1]:
        first, second = second, first
    if d == (1, 0) and first[0] < second[0]:
        first, second = second, first
    if d == (0, -1) and first[1] > second[1]:
        first, second = second, first
    if d == (-1, 0) and first[0] > second[0]:
        first, second = second, first


    def move(p):
        red_or_blue = tab[p[0]][p[1]]
        tab[p[0]][p[1]] = '.'

        m_p = p
        while tab[m_p[0]][m_p[1]] == '.':
            m_p = plus(m_p, d)

        if tab[m_p[0]][m_p[1]] != 'O':
            m_p = minus(m_p, d)
            tab[m_p[0]][m_p[1]] = red_or_blue


    move(first)
    move(second)


def check(tab):
    red_exist, blue_exist = False, False
    for i in range(n):
        for j in range(m):
            if tab[i][j] == 'R':
                red_exist = True
            if tab[i][j] == 'B':
                blue_exist = True

    if red_exist and blue_exist:
        # nothing
        return 2
    elif not red_exist and blue_exist:
        # success
        return 1
    else:
        # fail
        return 0


def can_go(tab, d):
    for i in range(n):
        for j in range(m):
            if tab[i][j] == 'R' or tab[i][j] == 'B':
                next_p = plus((i,j), d)
                if tab[next_p[0]][next_p[1]] == '.' or tab[next_p[0]][next_p[1]] == 'O':
                    return True
    return False


min_depth = float('inf')


que = deque([(table, 0)])
while que:
    now_table, depth = que.popleft()
    if depth > 10:
        continue

    c = check(now_table)  # long time
    if c == 0:
        continue
    if c == 1 and min_depth > depth:
        min_depth = depth
        continue

    for d in dxy:
        if can_go(now_table, d):
            new_table = [line[:] for line in now_table]  # long time
            go(new_table, d)
            que.append((new_table, depth + 1))



print(min_depth if min_depth != float('inf') else -1)




