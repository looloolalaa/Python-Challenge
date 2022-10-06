# moving coordinates (needed starting point)
from itertools import combinations


def solution(line):
    def cross(a, b):
        A, B, E = a
        C, D, F = b
        if A * D - B * C == 0:
            return False

        x = (B * F - E * D) / (A * D - B * C)
        y = (E * C - A * F) / (A * D - B * C)
        if x % 1 != 0 or y % 1 != 0:
            return False
        return (int(x), int(y))

    int_cross = set()
    for a, b in combinations(line, 2):
        c = cross(a, b)
        if c != False:
            int_cross.add(c)
    width = max(int_cross, key=lambda x: x[0])[0] - min(int_cross, key=lambda x: x[0])[0] + 1
    height = max(int_cross, key=lambda x: x[1])[1] - min(int_cross, key=lambda x: x[1])[1] + 1
    zero = (min(int_cross, key=lambda x: x[0])[0], max(int_cross, key=lambda x: x[1])[1])

    stars = [['.' for _ in range(width)] for _ in range(height)]
    for i in int_cross:
        stars[zero[1] - i[1]][i[0] - zero[0]] = '*'
    return [''.join(s) for s in stars]


if __name__ == '__main__':
    print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))