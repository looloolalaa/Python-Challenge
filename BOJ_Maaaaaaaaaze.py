# 3차원 미로 최단거리 + 판 회전 (dfs)
from itertools import permutations
from collections import deque

board_init = [[input().split() for _ in range(5)] for _ in range(5)]

dist = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(5)]

dxyz = [[0,0,1], [0,0,-1], [1,0,0], [-1,0,0], [0,1,0], [0,-1,0]]
def valid(p):
    return 0<=p[0]<5 and 0<=p[1]<5 and 0<=p[2]<5

def get_min_dist():
    global ans
    if board[0][0][0] == '0' or board[4][4][4] == '0':
        return -1

    for x in range(5):
        for y in range(5):
            for z in range(5):
                dist[x][y][z] = -1

    que = deque([(0,0,0)])
    dist[0][0][0] = 0
    while que:
        p = que.popleft()
        for d in dxyz:
            a = p[0]+d[0], p[1]+d[1], p[2]+d[2]
            if valid(a) and board[a[0]][a[1]][a[2]] == '1' and dist[a[0]][a[1]][a[2]] == -1:
                dist[a[0]][a[1]][a[2]] = dist[p[0]][p[1]][p[2]] + 1
                if dist[a[0]][a[1]][a[2]] < ans:
                    que.append(a)

    return dist[4][4][4]


def rotated(arr):
    return list(zip(*arr[::-1]))


ans = float('inf')
board = [[['-1' for _ in range(5)] for _ in range(5)] for _ in range(5)]
for p in permutations(range(5), 5):
    for i in range(5):
        board[i] = board_init[p[i]]

    def dfs(i):
        if i == 5:
            mini = get_min_dist()
            if mini != -1:
                global ans
                ans = min(ans, mini)
                if mini == 12:
                    print(12)
                    exit(0)
            return

        for _ in range(4):
            board[i] = rotated(board[i])
            dfs(i+1)

    dfs(0)

print(-1 if ans == float('inf') else ans)

