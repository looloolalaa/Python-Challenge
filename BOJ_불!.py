# BFS 횟수
from collections import deque

R, C = map(int, input().split())
table = [list(input()) for _ in range(R)]

my_que = deque()
fire_que = deque()

for i in range(R):
    for j in range(C):
        if table[i][j] == 'J':
            my_que.append((i, j))
        if table[i][j] == 'F':
            fire_que.append((i, j))

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def valid(p):
    return 0 <= p[0] < R and 0 <= p[1] < C

def move_fire():
    for _ in range(len(fire_que)):
        now = fire_que.popleft()
        for d in dxy:
            a = now[0]+d[0], now[1]+d[1]
            if valid(a) and (table[a[0]][a[1]] == '.' or table[a[0]][a[1]] == 'J'):
                table[a[0]][a[1]] = 'F'
                fire_que.append(a)


def move_me():
    for _ in range(len(my_que)):
        now = my_que.popleft()
        for d in dxy:
            a = now[0] + d[0], now[1] + d[1]
            if valid(a) and table[a[0]][a[1]] == '.':
                table[a[0]][a[1]] = 'J'
                my_que.append(a)


for k in range(R+C):
    if not my_que:
        print('IMPOSSIBLE')
        break

    for i, j in my_que:
        if i == 0 or i == R-1 or j == 0 or j == C-1:
            print(k + 1)
            # print(i, j)
            exit(0)

    move_fire()
    move_me()

