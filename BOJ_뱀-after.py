# 뱀 큐
from collections import deque

N = int(input())
K = int(input())
apples = set()
for _ in range(K):
    i, j = map(int, input().split())
    apples.add((i, j))

L = int(input())
directions = {}
for _ in range(L):
    s = input().split()
    directions[int(s[0])] = s[1]

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def valid(p):
    return 1<=p[0]<=N and 1<=p[1]<=N

snake = deque([(1, 1)])
time = 0
d = 0
while True:
    # print(time, snake)
    if time in directions:
        d = (d+1)%4 if directions[time] == 'D' else (d-1 + 4)%4

    head = snake[-1]
    new_head = head[0]+dxy[d][0], head[1]+dxy[d][1]
    if not valid(new_head) or new_head in snake:
        break

    if new_head in apples:
        apples.remove(new_head)
        snake.append(new_head)
    else:
        snake.append(new_head)
        snake.popleft()

    time += 1

print(time+1)
