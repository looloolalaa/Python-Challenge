# 테트리스 시뮬레이션
dxy = {1: [-1, 0], 2: [-1, -1], 3: [0, -1], 4: [1, -1], 5: [1, 0], 6: [1, 1], 7: [0, 1], 8: [-1, 1]}
direct = {}


def get_can():
    result = []
    temp = [-1 for _ in range(len(zero_pos))]

    def dfs(i):
        if i == len(temp):
            result.append(temp.copy())
            return
        for j in [1, 2, 3, 4]:
            temp[i] = j
            dfs(i + 1)

    dfs(0)
    return result


def valid(p):
    return 0 <= p[0] < 101 and 0 <= p[1] < 4


init_table = [[0 for _ in range(4)] for _ in range(101)]

# blocks = [[1, 1], [1, 2], [2, 0], .. , [3, 0], [7, 2]]
# zero_pos = [2, 3, 17, 89]
# can = [[1,1,1,1], [1,1,1,2], [1,1,1,3], ... , [4,4,4,4]]

blocks = []
zero_pos = []
n = int(input())
for i in range(8):
    direct[i + 1] = list(map(int, input().split()))
for _ in range(n):
    blocks.append(list(map(int, input().split())))

for i in range(n):
    if blocks[i][1] == 0:
        zero_pos.append(i)

can = get_can()
candis = []
if len(zero_pos) == 0:
    candis.append(blocks)
else:
    for c in can:
        temp = [block[:] for block in blocks]
        for i in range(len(zero_pos)):
            temp[zero_pos[i]][1] = c[i]
        candis.append(temp)


def get_score(order):
    # order == [[1, 1], [1, 2], [1, 3], [2, 3], ...]
    table = [row[:] for row in init_table]
    score = 0

    def drop(block):
        # block == [3, 4]
        col = block[1] - 1
        for i in range(100, -1, -1):
            if table[i][col] == 0:
                table[i][col] = block[0]
                return

    def line():
        count = 0
        for i in range(100, -1, -1):
            if all(num != 0 for num in table[i]):
                count += 1
                table[i] = [0, 0, 0, 0]
            else:
                break
        return count

    def gravity():
        for j in range(4):
            bottom = []
            for i in range(100, -1, -1):
                if table[i][j] != 0:
                    bottom.append(table[i][j])
                    table[i][j] = 0

            for k in range(len(bottom)):
                table[100 - k][j] = bottom[k]

    def move():
        new_table = [row[:] for row in init_table]
        for i in range(101):
            for j in range(4):
                if table[i][j] != 0:
                    first_valid_a = -1, -1
                    for d in direct[table[i][j]]:
                        a = (i + dxy[d][0], j + dxy[d][1])
                        if valid(a):
                            first_valid_a = a
                            break

                    if new_table[first_valid_a[0]][first_valid_a[1]] == 0:
                        new_table[first_valid_a[0]][first_valid_a[1]] = table[i][j]
                    else:
                        new_table[first_valid_a[0]][first_valid_a[1]] = min(
                            new_table[first_valid_a[0]][first_valid_a[1]], table[i][j])

        return new_table

    # drop([3, 4])
    # drop([1, 4])
    # drop([8, 4])
    # drop([7, 3])
    # drop([2, 1])
    # drop([6, 3])
    # drop([4, 2])

    # drop([2, 1])
    # drop([6, 2])
    # drop([7, 4])

    # print(line())
    # gravity()
    # table = move()
    # for t in table[95:]:
    #     print(t)

    for block in order:
        drop(block)
        score += line()
        gravity()
        table = move()
        gravity()
        score += line()
        gravity()

    return score


# print(get_score(candis[0]))
print(max([get_score(c) for c in candis]))
