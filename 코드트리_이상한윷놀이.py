# 시뮬레이션 디버깅: 문제다시보기 + 작은수디버깅
n, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

table = [[[] for _ in range(n)] for _ in range(n)]
positions = []
directions = []
for i in range(k):
    x, y, d = map(int, input().split())
    positions.append((x - 1, y - 1))
    table[x - 1][y - 1].append(i)
    directions.append(d)

# Write your code here!

dxy = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]
def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n

def go(i):
    pos = positions[i]
    stack = table[pos[0]][pos[1]]
    p = stack.index(i)
    target = stack[p:]
    remain = stack[:p]

    di = directions[i]
    next_pos = (pos[0] + dxy[di][0], pos[1] + dxy[di][1])

    # blue
    if not valid(next_pos) or board[next_pos[0]][next_pos[1]] == 2:
        new_di = di - 1 if di % 2 == 0 else di + 1
        directions[i] = new_di
        next_next_pos = (pos[0] + dxy[new_di][0], pos[1] + dxy[new_di][1])
        if not valid(next_next_pos) or board[next_next_pos[0]][next_next_pos[1]] == 2:
            return False
        elif board[next_next_pos[0]][next_next_pos[1]] == 1:
            target.reverse()
            table[next_next_pos[0]][next_next_pos[1]] += target
            table[pos[0]][pos[1]] = remain
            for t in target:
                positions[t] = next_next_pos

            if len(table[next_next_pos[0]][next_next_pos[1]]) >= 4:
                return True

        elif board[next_next_pos[0]][next_next_pos[1]] == 0:
            table[next_next_pos[0]][next_next_pos[1]] += target
            table[pos[0]][pos[1]] = remain
            for t in target:
                positions[t] = next_next_pos

            if len(table[next_next_pos[0]][next_next_pos[1]]) >= 4:
                return True

    # white
    elif board[next_pos[0]][next_pos[1]] == 0:
        table[next_pos[0]][next_pos[1]] += target
        table[pos[0]][pos[1]] = remain
        for t in target:
            positions[t] = next_pos

        if len(table[next_pos[0]][next_pos[1]]) >= 4:
            return True

    # red
    elif board[next_pos[0]][next_pos[1]] == 1:
        target.reverse()
        table[next_pos[0]][next_pos[1]] += target
        table[pos[0]][pos[1]] = remain
        for t in target:
            positions[t] = next_pos

        if len(table[next_pos[0]][next_pos[1]]) >= 4:
            return True

    return False


turn = 1
while turn <= 1000:
    for i in range(k):
        if go(i):
            print(turn)
            exit(0)
    turn += 1

print(-1)