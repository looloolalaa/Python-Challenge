# 4차원배열 BFS 최단거리
from collections import deque

n, m, c = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
car = list(map(lambda x: int(x) - 1, input().split()))
infos = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

dist = [[0 for _ in range(n)] for _ in range(n)]

dxy = [[-1, 0], [0, -1], [0, 1], [1, 0]]


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


def bfs(start):
    di = [[-1 for _ in range(n)] for _ in range(n)]
    di[start[0]][start[1]] = 0
    que = deque([start])
    while que:
        now = que.popleft()
        for d in dxy:
            a = now[0] + d[0], now[1] + d[1]
            if valid(a) and table[a[0]][a[1]] == 0 and di[a[0]][a[1]] == -1:
                di[a[0]][a[1]] = di[now[0]][now[1]] + 1
                que.append(a)

    dist[start[0]][start[1]] = [d[:] for d in di]


for i in range(n):
    for j in range(n):
        bfs((i, j))

people = set(range(m))


def find_nearest():
    return min(people, key=lambda i: (dist[car[0]][car[1]][infos[i][0]][infos[i][1]], infos[i][0], infos[i][1]))


while people:
    person = find_nearest()
    info = infos[person]
    a = dist[car[0]][car[1]][info[0]][info[1]]
    b = dist[info[0]][info[1]][info[2]][info[3]]

    if a == -1 or c < a + b:
        print(-1)
        exit(0)

    car = [info[2], info[3]]
    c -= (a + b)
    c += 2 * b
    people.remove(person)

print(c)
