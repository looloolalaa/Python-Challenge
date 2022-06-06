"""
key 를 왼쪽위 모서리 부터 돌려 가면서 lock 확인
"""


def solution(key, lock):
    m, n = len(key), len(lock)
    big_lock = [[0 for _ in range(2 * m + n)] for _ in range(2 * m + n)]
    for i in range(n):
        for j in range(n):
            big_lock[i + m][j + m] = lock[i][j]


    def rotate(arr):
        return list(zip(*arr[::-1]))

    def isRight():
        for i in range(n):
            for j in range(n):
                if big_lock[i + m][j + m] != 1:
                    return False
        return True

    def attach(pos):
        for i in range(m):
            for j in range(m):
                big_lock[i+pos[0]][j+pos[1]] += key[i][j]

    def detach(pos):
        for i in range(m):
            for j in range(m):
                big_lock[i + pos[0]][j + pos[1]] -= key[i][j]


    for i in range(m+n):
        for j in range(m+n):
            for _ in range(4):
                key = rotate(key)
                attach((i, j))
                if isRight():
                    return True
                detach((i, j))
    return False


if __name__ == '__main__':
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))