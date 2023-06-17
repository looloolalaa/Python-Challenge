# key가 여러개 일때 dfs 경우가 너무 많아짐
# => "key포함 상태" 를 가지고 bfs 한번
from collections import deque

N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]

start = -1, -1
for i in range(N):
    for j in range(M):
        if table[i][j] == '0':
            start = i, j

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def valid(p):
    return 0 <= p[0] < N and 0 <= p[1] < M

# key 6개
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2**6)]

visited[0][start[0]][start[1]] = True
que = deque([(start, 0, 0)])
while que:
    p, keys, dist = que.popleft()
    # print(p, keys, dist)
    if table[p[0]][p[1]] == '1':
        print(dist)
        exit()

    for d in dxy:
        a = p[0]+d[0], p[1]+d[1]
        if valid(a):
            value = table[a[0]][a[1]]
            if (value == '.' or value == '1' or value == '0') and not visited[keys][a[0]][a[1]]:
                visited[keys][a[0]][a[1]] = True
                que.append((a, keys, dist + 1))
            elif 'a' <= value <= 'f':
                i = ord(value) - ord('a')
                new_keys = keys | (1 << i)
                if not visited[new_keys][a[0]][a[1]]:
                    visited[new_keys][a[0]][a[1]] = True
                    que.append((a, new_keys, dist + 1))
            elif 'A' <= value <= 'F' and not visited[keys][a[0]][a[1]]:
                i = ord(value) - ord('A')
                if keys & (1 << i) != 0:
                    visited[keys][a[0]][a[1]] = True
                    que.append((a, keys, dist + 1))


print(-1)

