# 놓을 수 있는 숫자들 구하기
def nums(i, j):
    already = [False for _ in range(10)]
    for y in range(9):
        already[arr[i][y]] = True
    for x in range(9):
        already[arr[x][j]] = True
    a, b = i//3*3, j//3*3
    for x in range(3):
        for y in range(3):
            already[arr[a+x][b+y]] = True

    return [n for n in range(1, 10) if not already[n]]

arr = [list(map(int, input())) for _ in range(9)]

def dfs(idx):
    if idx == 81:
        for a in arr:
            print(''.join(map(str, a)))
        exit(0)

    i, j = idx//9, idx%9
    if arr[i][j] != 0:
        dfs(idx+1)
    else:
        for n in nums(i, j):
            arr[i][j] = n
            dfs(idx+1)
            arr[i][j] = 0


dfs(0)

