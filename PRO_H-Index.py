"""
bisect
"""
from bisect import bisect_left


def solution(citations):
    n = len(citations)
    citations.sort()
    l = 0
    for l in range(1001):
        i = bisect_left(citations, l)
        up_count = n-i
        if not (up_count >= l and i<=l):
            break
    return l-1


if __name__ == '__main__':
    print(solution([3, 0, 6, 1, 5]))