from collections import deque

n = int(input())
k = int(input())

table = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    i, j = map(int, input().split())
    table[i-1][j-1] = 1

change = {}
l = int(input())
for _ in range(l):
    t, left_or_right = input().split()
    change[int(t)] = 1 if left_or_right == 'D' else -1


def plus(p, d):
    return p[0] + d[0], p[1] + d[1]


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


arrows = [(0, 1), (1, 0), (0, -1), (-1, 0)]

table[0][0] = -1
snake = deque([(0, 0)])
a = 0
time = 0

while True:
    time += 1
    next_head = plus(snake[-1], arrows[a])
    if time in change:
        a = (a + change[time] + 4) % 4

    # 벽
    if not valid(next_head):
        break
    # 몸
    if table[next_head[0]][next_head[1]] == -1:
        break

    # 사과
    if table[next_head[0]][next_head[1]] == 1:
        table[next_head[0]][next_head[1]] = -1
        snake.append(next_head)

    # 바닥
    if table[next_head[0]][next_head[1]] == 0:
        table[next_head[0]][next_head[1]] = -1
        table[snake[0][0]][snake[0][1]] = 0

        snake.append(next_head)
        snake.popleft()


print(time)