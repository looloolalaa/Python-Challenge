# 4방향 탐색 후 for else
n, m = map(int, input().split())
x,y,d = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(n)]
dxy = [[-1,0], [0,1], [1,0], [0,-1]]
def valid(i, j):
    return 0<=i<n and 0<=j<m

table[x][y] = 2
while True:
    for _ in range(4):
        d = (d-1+4)%4
        a, b = x+dxy[d][0], y+dxy[d][1]
        if valid(a, b) and table[a][b] == 0:
            x,y = a,b
            table[a][b] = 2
            break
    else:
        back = x-dxy[d][0], y-dxy[d][1]
        if not valid(back[0], back[1]) or table[back[0]][back[1]] == 1:
            break
        else:
            x,y = back

ans = 0
for i in range(n):
    for j in range(m):
        if table[i][j] == 2:
            ans += 1
print(ans)