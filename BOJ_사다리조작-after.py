# dfs 사다리 내리기
N, M, H = map(int, input().split())
ladder = [[False for _ in range(N+1)] for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b] = True

def check():
    for n in range(N):
        j = n
        for i in range(H):
            if ladder[i][j]:
                j -= 1
            elif ladder[i][j+1]:
                j += 1
        if j != n:
            return False
    return True


def valid(p):
    return not ladder[p[0]][p[1]] and not ladder[p[0]][p[1]-1] and not ladder[p[0]][p[1]+1]

def dfs(depth, maxDepth):
    if depth == maxDepth:
        if check():
            print(depth)
            exit(0)
        return

    can_put = []
    for j in range(1, N):
        i = 0
        while i < H:
            if valid((i, j)):
                can_put.append((i, j))
                while i < H and not ladder[i][j-1] and not ladder[i][j+1]:
                    i += 1
            i += 1

    for p in can_put:
        ladder[p[0]][p[1]] = True
        dfs(depth+1, maxDepth)
        ladder[p[0]][p[1]] = False

for select in range(4):
    dfs(0, select)
print(-1)
