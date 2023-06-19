# 선풍기 완전탐색 dfs로도 가능
from itertools import product

N, M = map(int, input().split())
init_table = [input().split() for _ in range(N)]

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def valid(p):
    return 0<=p[0]<N and 0<=p[1]<M


dirs = {
    '1': [[0], [1], [2], [3]],
    '2': [[0, 2], [1, 3]],
    '3': [[0, 1], [1, 2], [2, 3], [3, 0]],
    '4': [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    '5': [[0, 1, 2, 3]]
}

poses = []
types = []
for i in range(N):
    for j in range(M):
        if '1' <= init_table[i][j] <= '5':
            poses.append((i, j))
            types.append(init_table[i][j])


k = len(types)
result = float('inf')

cases = [dirs[t] for t in types]
for candi in product(*cases):
    table = [line[:] for line in init_table]

    def go(i):
        for d in candi[i]:
            now = poses[i]
            while valid(now) and table[now[0]][now[1]] != '6':
                table[now[0]][now[1]] = '#'
                now = now[0]+dxy[d][0], now[1]+dxy[d][1]


    for i in range(k):
        go(i)

    res = 0
    for i in range(N):
        for j in range(M):
            if table[i][j] == '0':
                res += 1
    result = min(result, res)

    # print(candi)
    # for t in table:
    #     print(t)

print(result)