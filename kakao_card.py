import itertools

Board = []
Cards = {}
Moves = {(0, 1): lambda x: x[1] < 3,
         (1, 0): lambda x: x[0] < 3,
         (0, -1): lambda x: x[1] > 0,
         (-1, 0): lambda x: x[0] > 0}

def isValid(p):
    return 0 <= p[0] < 4 and 0 <= p[1] < 4

def get_nexts(board, dis, here):
    global Moves
    nexts = []
    for move, cond in Moves.items():
        next_pos = [here[0]+move[0], here[1]+move[1]]
        if isValid(next_pos):
            if dis[next_pos[0]][next_pos[1]] == 0:
                nexts.append(next_pos)
            if board[next_pos[0]][next_pos[1]] == 0:
                ctrl_pos = next_pos[:]
                while cond(ctrl_pos) and board[ctrl_pos[0]][ctrl_pos[1]] == 0:
                    ctrl_pos = [ctrl_pos[0] + move[0], ctrl_pos[1] + move[1]]
                if dis[ctrl_pos[0]][ctrl_pos[1]] == 0:
                    nexts.append(ctrl_pos)

    return nexts

def BFS(board, s, e):
    dis = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]

    que = []
    que.append(s)
    dis[s[0]][s[1]] = 1
    while que:
        here = que.pop(0)
        here_dis = dis[here[0]][here[1]]
        nexts = get_nexts(board, dis, here)
        for n in nexts:
            que.append(n)
            dis[n[0]][n[1]] = here_dis + 1
            if e == n:
                return dis[e[0]][e[1]] - 1

    return dis[e[0]][e[1]] - 1


def total_dis(order, case, start, minimum):
    global Cards
    board = [row[:] for row in Board]
    here = start[:]
    total = 0
    for card, first in zip(order, case):
        pos = Cards[card]
        xcard, ycard = pos[0], pos[1]
        if first == 1:
            xcard, ycard = ycard, xcard
        total += BFS(board, here, xcard) + BFS(board, xcard, ycard) + 2
        if total >= minimum:
            break
        board[xcard[0]][xcard[1]], board[ycard[0]][ycard[1]] = 0, 0
        here = ycard
    return total


def solution(board, r, c):
    global Board, Cards
    Board = board
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val != 0:
                if val in Cards:
                    Cards[val].append([i, j])
                else:
                    Cards[val] = [[i, j]]
    orders = list(itertools.permutations(Cards, len(Cards)))
    cases = list(itertools.product([0,1], repeat=len(Cards)))

    minimum = float('inf')
    for order in orders:
        for case in cases:
            temp = total_dis(order, case, [r, c], minimum)
            if minimum > temp:
                minimum = temp

    # print(cards)
    # print(orders)
    # print(cases)

    return minimum


if __name__ == '__main__':
    # board = [[1,0,0,3],
    #          [2,0,0,0],
    #          [0,0,0,2],
    #          [3,0,1,0]]
    board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
    r, c = 0, 1
    print(solution(board, r, c))

