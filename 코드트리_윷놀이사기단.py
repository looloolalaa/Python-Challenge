# 윷놀이 보드
moves = list(map(int, input().split()))

pos = [(0, -1) for _ in range(4)]


board = [
    [2,4,6,8, 10, 12,14,16,18, 20, 22,24,26,28, 30, 32,34,36,38, 40],
    [13,16,19],
    [22,24,25,30,35],
    [28,27,26]
]


# 한 칸 다음의 위치
def next_p(p):
    if p == (-1, -1):
        return (-1, -1)

    if p == (0, 4):
        return (1, 0)
    elif p == (0, 9):
        return (2, 0)
    elif p == (0, 14):
        return (3, 0)
    elif p == (0, 19):
        return (-1, -1)


    elif p == (1, 2):
        return (2, 2)

    elif p == (2, 4):
        return (0, 19)  # 40

    elif p == (3, 2):
        return (2, 2)

    else:
        return p[0], p[1]+1


result = 0
def dfs(i, s):
    if i == 10:
        global result
        result = max(result, s)
        return

    for horse in range(4):
        if pos[horse] == (-1, -1):
            continue

        new_p = pos[horse]
        if pos[horse][0] == 0 and pos[horse][1] != 4 and pos[horse][1] != 9 and pos[horse][1] != 14:
            new_p = new_p[0], new_p[1]+moves[i]
            if new_p[1] > 19:
                new_p = (-1, -1)
        else:
            for _ in range(moves[i]):
                new_p = next_p(new_p)


        if new_p != (-1, -1) and new_p in pos:
            continue

        # pos move, score
        before_pos = pos[horse]
        score = 0 if new_p == (-1, -1) else board[new_p[0]][new_p[1]]

        pos[horse] = new_p
        dfs(i + 1, s + score)
        pos[horse] = before_pos



dfs(0, 0)
print(result)
