# 2번 combi
from itertools import combinations

N, M, G, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]

def visit():
    for r in red_que:
        visited[r[0]][r[1]] = True
    for g in green_que:
        visited[g[0]][g[1]] = True

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def valid(p):
    return 0 <= p[0] < N and 0 <= p[1] < M

def get_next(que):
    res = set()
    while que:
        now = que.pop()
        for d in dxy:
            a = now[0]+d[0], now[1]+d[1]
            if valid(a) and board[a[0]][a[1]] != 0 and not visited[a[0]][a[1]]:
                res.add(a)
    return res

def get_flower_cnt():
    global red_que, green_que, visited
    visited = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0
    visit()
    while red_que or green_que:
        red_next = get_next(red_que)
        green_next = get_next(green_que)

        for flower in red_next & green_next:
            cnt += 1
            red_next.remove(flower)
            green_next.remove(flower)
            visited[flower[0]][flower[1]] = True

        red_que = red_next
        green_que = green_next
        visit()

    return cnt


candi = set()
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            candi.add((i, j))

ans = 0
for reds in combinations(candi, R):
    temp = candi.copy()
    remain = temp - set(reds)
    for greens in combinations(remain, G):
        red_que = set(reds)
        green_que = set(greens)
        ans = max(ans, get_flower_cnt())

print(ans)