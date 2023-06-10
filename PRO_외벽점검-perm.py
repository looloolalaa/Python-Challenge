# 원형 구조 => 2배로 늘리기
from itertools import permutations
from collections import deque

def solution(n, weak, dist):
    weak_count, dist_count = len(weak), len(dist)
    weak += [w+n for w in weak]

    def people_count(w, o):
        w, o = deque(w), deque(o)

        end = -1
        while w and o:
            point = w.popleft()
            if end < point:
                end = point + o.popleft()

        while w and w[0] <= end:
            w.popleft()

        if w:
            return float('inf')
        return dist_count-len(o)

    mini = float('inf')
    for i in range(weak_count):
        for order in permutations(dist, len(dist)):
            # print(weak[i:i+weak_count], order)
            mini = min(mini, people_count(weak[i:i+weak_count], order))

    return -1 if mini == float('inf') else mini


