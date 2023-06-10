# 자물쇠 크기 늘리기
def solution(key, lock):
    m, n = len(key), len(lock)

    def rotated(arr):
        return list(zip(*arr[::-1]))

    big_lock = [[0 for _ in range(n + 2 * m)] for _ in range(n + 2 * m)]
    for i in range(n):
        for j in range(n):
            big_lock[i + m][j + m] = lock[i][j]

    def attach(x, y):
        for i in range(m):
            for j in range(m):
                big_lock[i + x][j + y] += key[i][j]

    def detach(x, y):
        for i in range(m):
            for j in range(m):
                big_lock[i + x][j + y] -= key[i][j]

    def all_one():
        for i in range(n):
            for j in range(n):
                if big_lock[i + m][j + m] != 1:
                    return False
        return True

    for _ in range(4):
        key = rotated(key)
        for x in range(n + m + 1):
            for y in range(n + m + 1):
                attach(x, y)
                if all_one():
                    return True
                detach(x, y)

    return False