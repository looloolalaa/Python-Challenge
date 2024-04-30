# 놓을 수 있는 숫자 valid 확인하기
def valid(i, j, n):
    for y in range(9):
        if arr[i][y] == n:
            return False
    for x in range(9):
        if arr[x][j] == n:
            return False
    a, b = i//3*3, j//3*3
    for x in range(3):
        for y in range(3):
            if arr[a+x][b+y] == n:
                return False

    return True

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
        for n in range(1, 10):
            if valid(i, j, n):
                arr[i][j] = n
                dfs(idx+1)
                arr[i][j] = 0


dfs(0)

