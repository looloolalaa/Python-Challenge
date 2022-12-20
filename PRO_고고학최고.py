# 제일 위 라인의 케이스들 부터 시작해서
# 아래로 한줄씩 내려가기
from itertools import product


def solution(clockHands):
    result = float('inf')
    n = len(clockHands)
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def valid(p):
        return 0 <= p[0] < n and 0 <= p[1] < n

    candis = list(product([0, 1, 2, 3], repeat=n))
    for c in candis:
        rotate = [c]
        line = clockHands[0][:]
        for j in range(n):
            line[j] = (line[j] + c[j]) % 4
            if j != 0:
                line[j - 1] = (line[j - 1] + c[j]) % 4
            if j != n - 1:
                line[j + 1] = (line[j + 1] + c[j]) % 4

        # line => rotated
        rotated = [line[:]]

        for i in range(1, n):
            need = [(4 - l) % 4 for l in line[:]]
            rotate.append(need[:])
            line = clockHands[i]
            for j in range(n):
                line[j] = (line[j] + need[j]) % 4
                if j != 0:
                    line[j - 1] = (line[j - 1] + need[j]) % 4
                if j != n - 1:
                    line[j + 1] = (line[j + 1] + need[j]) % 4
            rotated.append(line[:])

        if all(v == 0 for v in line for line in rotated):
            result = min(result, sum(sum(line) for line in rotate))

    print(result)
    return -1