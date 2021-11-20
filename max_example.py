def maxs():
    temp = [1, 2, 3, 4, 55, 8, 7, 3, 4, 4444, 1, 0]
    big = -float('inf')

    # 최대값을 가지는 키들 O(n)
    max_indices = []
    for i, val in enumerate(temp):
        if big == val:
            max_indices.append(i)
        elif big < val:
            big = val
            max_indices = [i]
    print(max_indices)


    temp = {'hi': -8, 'bye': 2, 'what': 3, 'zz': 4444, 'xx': 6, 'oo': 4444}

    # 최대값을 가지는 키들 O(2n) = O(n)
    max_val = max(temp.values())
    max_keys = [key for key, value in temp.items() if value == max_val]
    print(max_keys)


    # 최대값을 가지는 키(여러개면 제일 앞에 키)
    print(max(temp, key=lambda x: temp[x]))
    print(max(temp, key=temp.get))


def max_with_key():
    board = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]]

    def isValid(p):
        return 0 <= p[0] < len(board) and 0 <= p[1] < len(board[0])

    center = (2, 2)
    near = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    candi = []
    for n in near:
        new_pos = (center[0]+n[0], center[1]+n[1])
        if isValid(new_pos):
            candi.append(new_pos)
    print(max(candi, key=lambda x: board[x[0]][x[1]]))

    # one-line: may be hard to read
    # print(max([new_pos for n in near if isValid(new_pos := (center[0] + n[0], center[1] + n[1]))], key=lambda x: board[x[0]][x[1]]))


if __name__ == '__main__':
    max_with_key()