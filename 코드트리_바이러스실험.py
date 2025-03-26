# 나이순 바이러스
n, m, k = map(int, input().split())

nutrients = [list(map(int, input().split())) for _ in range(n)]
virus = [[[] for _ in range(n)] for _ in range(n)]
food = [[5 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, age = map(int, input().split())
    virus[r - 1][c - 1].append(age)

dxy = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


for i in range(n):
    for j in range(n):
        virus[i][j].sort()

dead = [[[] for _ in range(n)] for _ in range(n)]


def eat():
    for i in range(n):
        for j in range(n):
            for a in range(len(virus[i][j])):
                age = virus[i][j][a]
                if age <= food[i][j]:
                    food[i][j] -= age
                    virus[i][j][a] += 1
                else:
                    dead[i][j] += virus[i][j][a:]
                    virus[i][j] = virus[i][j][:a]
                    break


def die():
    for i in range(n):
        for j in range(n):
            for age in dead[i][j]:
                food[i][j] += age // 2
            dead[i][j] = []


def spread():
    cnt = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for age in virus[i][j]:
                if age % 5 == 0:
                    cnt[i][j] += 1

    for i in range(n):
        for j in range(n):
            for d in dxy:
                a = i + d[0], j + d[1]
                if valid(a):
                    for _ in range(cnt[i][j]):
                        virus[a[0]][a[1]].append(1)

    for i in range(n):
        for j in range(n):
            virus[i][j].sort()


def plus():
    for i in range(n):
        for j in range(n):
            food[i][j] += nutrients[i][j]


for _ in range(k):
    eat()
    die()
    spread()
    plus()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(virus[i][j])
print(ans)
