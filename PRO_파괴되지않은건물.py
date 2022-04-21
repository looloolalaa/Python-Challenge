"""
2차원 누적합
dxy
= [[0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0]]
(1,1) ~ (2,2) +d

[[0,0,0,0],
 [0,d,0,-d],
 [0,0,0,0],
 [0,-d,0,d]]
dxy[i][j] += dxy[i-1][j] + dxy[i][j-1] - dxy[i-1][j-1]
"""


def solution(board, skill):

    n, m = len(board), len(board[0])
    dxy = [[0 for _ in range(m+2)] for _ in range(n+2)]

    for s in skill:
        i1, j1, i2, j2, d = s[1], s[2], s[3], s[4], s[5]
        if s[0] == 1:
            d = -d
        dxy[i1+1][j1+1] += d
        dxy[i2+2][j2+2] += d
        dxy[i1+1][j2+2] += -d
        dxy[i2+2][j1+1] += -d

    for i in range(1, n+2):
        for j in range(1, m+2):
            dxy[i][j] += dxy[i-1][j]+dxy[i][j-1]-dxy[i-1][j-1]

    for i in range(n):
        for j in range(m):
            board[i][j] += dxy[i+1][j+1]

    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                count += 1
    return count


if __name__ == '__main__':
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    print(solution(board, skill))

    # for row in board:
    #     print(row)
