# 시뮬레이션 global
from itertools import combinations
from collections import deque

N, M, D = map(int, input().split())
board_initial = deque(list(map(int, input().split())) for _ in range(N))

empty = [0 for _ in range(M)]

def move():
    board.pop()
    board.appendleft(empty)

def dist(x, y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])


c = 0
board = deque()
people = ()
def attack():
    min_dists = [float('inf') for _ in range(3)]
    targets = [(-1, -1) for _ in range(3)]
    for j in range(M):
        for i in range(N):
            for k in range(3):
                if board[i][j] == 1:
                    d = dist(people[k], (i, j))
                    if d <= D and d < min_dists[k]:
                        min_dists[k] = d
                        targets[k] = (i, j)

    for i, j in set(targets):
        if (i, j) != (-1, -1):
            board[i][j] = 0
            global c
            c += 1

def count(peo):
    global c, people, board
    c = 0
    people = peo
    board = deque(b[:] for b in board_initial)
    for _ in range(N):
        attack()
        move()
    return c


ans = 0
for candi in combinations([i for i in range(M)], 3):
    people = [(N, candi[m]) for m in range(3)]
    ans = max(ans, count(people))
print(ans)