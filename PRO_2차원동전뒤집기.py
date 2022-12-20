# 1개의 열 뒤집는 경우 + 2개 열 경우 + .. + 다 뒤집는 경우
# 각 경우에서 target 에 맞도록 row 뒤집기
from itertools import combinations


def solution(beginning, target):
    row, col = len(beginning), len(beginning[0])

    temp = [i for i in range(col)]
    candis = []
    for l in range(col + 1):
        candis += combinations(temp, l)

    result = float('inf')
    for c in candis:
        flipped = [line[:] for line in beginning]
        for j in c:
            for i in range(row):
                flipped[i][j] = 1 if flipped[i][j] == 0 else 0

        need_row = []
        for i in range(row):
            if sum(a ^ b for a, b in zip(flipped[i], target[i])) > 0:
                need_row.append(i)

        for i in need_row:
            for j in range(col):
                flipped[i][j] = 1 if flipped[i][j] == 0 else 0

        if flipped == target:
            result = min(result, len(c) + len(need_row))

    return result if result != float('inf') else -1


if __name__ == '__main__':
    print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))