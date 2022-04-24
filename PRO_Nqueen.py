"""
2차원 배열 Backtracking
"""


def solution(n):
    table = [[True for _ in range(n)] for _ in range(n)]
    board = []

    def erase(t, p):
        x, y = p[0], p[1]
        for i in range(x+1, n):
            d = i-x
            t[i][y] = False
            if 0 <= y-d:
                t[i][y-d] = False
            if y+d < n:
                t[i][y+d] = False

    def check(t, i):
        if i == n-1 and True in t[i]:
            board.append(t)
            return
        if True not in t[i]:
            return

        for j in range(n):
            if t[i][j]:
                temp = [row[:] for row in t]
                erase(temp, (i, j))
                check(temp, i + 1)

    check(table, 0)
    return len(board)


if __name__ == '__main__':
    print(solution(10))