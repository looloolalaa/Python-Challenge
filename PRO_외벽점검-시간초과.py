# 15P8 겹치는 범위가 많아서 시간초과
from itertools import permutations


def solution(n, weak, dist):
    dist.sort(reverse=True)

    for num in range(len(dist) + 1):
        for candi in permutations(weak, num):
            all_range = []
            for d, start in zip(dist[:num], candi):
                if start + d >= n:
                    all_range.append(range(start, n))
                    all_range.append(range(0, start + d - n + 1))
                else:
                    all_range.append(range(start, start + d + 1))

            if all(any(w in r for r in all_range) for w in weak):
                return num

    return -1