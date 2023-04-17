# arrow: (1~8) + 3차원 배열 깊은 복사 ..
board = []
for _ in range(4):
    line = list(map(int, input().split()))
    temp = []
    for i in range(4):
        temp.append([line[2*i], line[2*i+1]])
    board.append(temp)

dxy = {1: [-1, 0], 2: [-1, -1], 3: [0, -1], 4: [1, -1], 5: [1, 0], 6: [1, 1], 7: [0, 1], 8: [-1, 1]}


def all_move(boa):
    board = [[[0, 0] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            board[i][j] = boa[i][j][:]

    def can_go(p):
        return 0 <= p[0] < 4 and 0 <= p[1] < 4 and 0 <= board[p[0]][p[1]][0] <= 16

    def move(p):
        arrow = board[p[0]][p[1]][1]
        for _ in range(8):
            if can_go((p[0]+dxy[arrow][0], p[1]+dxy[arrow][1])):
                break
            arrow = 1 if arrow == 8 else (arrow + 1)
        else:
            return

        board[p[0]][p[1]][1] = arrow

        next_p = p[0]+dxy[arrow][0], p[1]+dxy[arrow][1]
        get_out = [0, 0]
        if 1 <= board[next_p[0]][next_p[1]][0] <= 16 and board[next_p[0]][next_p[1]][1] != 0:
            get_out = board[next_p[0]][next_p[1]][:]

        board[next_p[0]][next_p[1]] = board[p[0]][p[1]][:]
        board[p[0]][p[1]] = get_out[:]


    def get_pos(num):
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == num and board[i][j][1] != 0:
                    return (i, j)
        return (-1, -1)

    for num in range(1, 17):
        p = get_pos(num)
        if p == (-1, -1):
            continue
        move(p)

    return board

def valid(p):
    return 0<=p[0]<4 and 0<=p[1]<4


result = 0
def dfs(boa, s):
    board = [[[0, 0] for _ in range(4)] for _ in range(4)]
    new_boa = all_move(boa)
    for i in range(4):
        for j in range(4):
            board[i][j] = new_boa[i][j][:]


    tag = -1, -1
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == -1:
                tag = (i, j)

    arrow = board[tag[0]][tag[1]][1]
    new_p = tag[0]+dxy[arrow][0], tag[1]+dxy[arrow][1]
    can_catch = []
    while valid(new_p):
        if 1 <= board[new_p[0]][new_p[1]][0] <= 16 and board[new_p[0]][new_p[1]][1] != 0:
            can_catch.append(new_p)
        new_p = new_p[0]+dxy[arrow][0], new_p[1]+dxy[arrow][1]

    if not can_catch:
        global result
        result = max(result, s)
        return

    for thief in can_catch:
        new_board = [[[0, 0] for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_board[i][j] = board[i][j][:]

        new_board[tag[0]][tag[1]] = [0, 0]
        sco = new_board[thief[0]][thief[1]][0]
        new_board[thief[0]][thief[1]][0] = -1
        dfs(new_board, s + sco)


score = board[0][0][0]
board[0][0][0] = -1

dfs(board, score)
print(result)

