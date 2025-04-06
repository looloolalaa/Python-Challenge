# 블럭 모양 만들기
blocks = [
    [[1,1,1,1]],
    [[1,1],[1,1]],
    [[1,1,1],[1,0,0]],
    [[1,0],[1,1],[0,1]],
    [[0,1,0],[1,1,1]],
    [[1,1,1],[0,0,1]],
    [[0,1],[1,1],[1,0]]
]

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

def score(block, p):
    a, b = len(block), len(block[0])
    res = 0
    for i in range(a):
        for j in range(b):
            if block[i][j] == 1:
                res += table[p[0]+i][p[1]+j]
    return res

ans = 0
def put(block):
    a, b = len(block), len(block[0])
    for i in range(n-a+1):
        for j in range(m-b+1):
            global ans
            ans = max(ans, score(block, (i, j)))

def rotated(arr):
    return list(zip(*arr[::-1]))

for block in blocks:
    now_block = block
    for _ in range(4):
        now_block = rotated(now_block)
        put(rotated(now_block))

print(ans)