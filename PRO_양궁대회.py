# 2^11 완전 탐색
from itertools import product


def solution(n, info):
    def valid(c):
        return n >= sum(i + 1 for i, get in zip(info, c) if get)

    def score_diff(c):
        a, b = 0, 0
        for i in range(11):
            if c[i] == 1:
                b += 10 - i
            if c[i] == 0:
                if info[i] != 0:
                    a += (10 - i)
        return b - a

    candis = list(product([0, 1], repeat=11))
    valids = list(filter(valid, candis))
    max_diff = max(score_diff(v) for v in valids)
    if max_diff <= 0:
        return [-1]

    results = list(filter(lambda v: score_diff(v) == max_diff, valids))
    result = sorted(results, key=lambda x: tuple(reversed(x)), reverse=True)[0]
    result = [0 if result[i] == 0 else info[i] + 1 for i in range(11)]
    if sum(result) < n:
        result[10] += n - sum(result)
    return result


if __name__ == '__main__':
    print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))