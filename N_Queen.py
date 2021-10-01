def solution1(n):
    board = [[1 for _ in range(n)] for _ in range(n)]
    moves = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    answer = []

    def isValid(p):
        return 0 <= p[0] < n and 0 <= p[1] < n

    def put(board, p):
        board[p[0]][p[1]] = -1
        for move in moves:
            next_pos = [p[0] + move[0], p[1] + move[1]]
            while isValid(next_pos):
                board[next_pos[0]][next_pos[1]] = 0
                next_pos = [next_pos[0] + move[0], next_pos[1] + move[1]]

    def can_pos(row):
        pos = []
        for j, val in enumerate(row):
            if val == 1:
                pos.append(j)
        return pos

    def queen(board, i):
        if i >= len(board):
            queen_pos = []
            for i, row in enumerate(board):
                print(row)
                for j, val in enumerate(row):
                    if val == -1:
                        queen_pos.append([i, j])
            answer.append(queen_pos)
            print()
            return

        row = board[i]
        put_pos = can_pos(row)
        if not put_pos:
            return
        else:
            for j in put_pos:
                copy_board = [row[:] for row in board]
                put(copy_board, [i, j])
                queen(copy_board, i + 1)

    queen(board, 0)
    return answer

def solution2(n):
    answer = []

    def right(board, row_index):
        # [1,2,3,-1]
        added = board[row_index]
        for i in range(row_index):
            if board[i] == added or row_index - i == abs(board[i]-added):
                return False
        return True


    def put(board):
        if board[-1] != -1:
            answer.append(board)
            return
        else:
            row_index = board.index(-1)
            for j in range(n):
                copy_board = board[:]
                copy_board[row_index] = j
                if right(copy_board, row_index):
                    put(copy_board)

    put([-1 for _ in range(n)])
    print(answer)
    return len(answer)


if __name__ == '__main__':
    print(solution2(4))