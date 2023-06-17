# 풀이는 맞지만 시간초과
from itertools import product, permutations
# from math import perm
# print(perm(10, 3) * (16**3))

def rotated(arr):
    return list(zip(*arr[::-1]))

n = int(input())
nums = []
colors = []
for _ in range(n):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    nums.append(temp)

    temp = []
    for _ in range(4):
        temp.append(list(input().split()))
    colors.append(temp)



result = 0
order = list(permutations([i for i in range(n)], 3))
for p in list(product(order, list(product(list(product([0, 1, 2, 3], repeat=2)), repeat=3)))):
    num_table = [[0 for _ in range(5)] for _ in range(5)]
    color_table = [['W' for _ in range(5)] for _ in range(5)]

    selected, rotate_pos = p

    # print(selected, rotate_pos)
    for i in range(3):
        k = selected[i]
        rotate, pos = rotate_pos[i]
        if pos == 0:
            pos = 0, 0
        elif pos == 1:
            pos = 0, 1
        elif pos == 2:
            pos = 1, 0
        elif pos == 3:
            pos = 1, 1


        num = nums[k]
        color = colors[k]
        for _ in range(rotate):
            num = rotated(num)
            color = rotated(color)


        for i in range(4):
            for j in range(4):
                num_table[i+pos[0]][j+pos[1]] += num[i][j]
                if num_table[i+pos[0]][j+pos[1]] < 0:
                    num_table[i + pos[0]][j + pos[1]] = 0
                elif num_table[i+pos[0]][j+pos[1]] > 9:
                    num_table[i + pos[0]][j + pos[1]] = 9

                if color[i][j] != 'W':
                    color_table[i + pos[0]][j + pos[1]] = color[i][j]

    # for line in num_table:
    #     print(line)
    # print()
    # for line in color_table:
    #     print(line)
    # print()

    r, b, g, y = 0, 0, 0, 0
    for i in range(5):
        for j in range(5):
            if color_table[i][j] == 'R':
                r += num_table[i][j]
            elif color_table[i][j] == 'B':
                b += num_table[i][j]
            elif color_table[i][j] == 'G':
                g += num_table[i][j]
            elif color_table[i][j] == 'Y':
                y += num_table[i][j]

    result = max(result, 7*r + 5*b + 3*g + 2*y)

print(result)
