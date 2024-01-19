# 최소최대힙 + counter
from collections import Counter
import heapq
import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    min_heap = []
    max_heap = []
    counter = Counter()

    k = int(input())
    for _ in range(k):
        com, num = input().split()
        if com == 'I':
            n = int(num)
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            counter[n] += 1

        elif num == '1':
            if not max_heap or not counter:
                continue

            maxi = -heapq.heappop(max_heap)
            while maxi not in counter and max_heap:
                maxi = -heapq.heappop(max_heap)

            counter[maxi] -= 1
            if counter[maxi] == 0:
                counter.pop(maxi)

        else:
            if not min_heap or not counter:
                continue

            mini = heapq.heappop(min_heap)
            while mini not in counter and min_heap:
                mini = heapq.heappop(min_heap)

            counter[mini] -= 1
            if counter[mini] == 0:
                counter.pop(mini)

    if not counter:
        print('EMPTY')
    else:
        maxi = -heapq.heappop(max_heap)
        while maxi not in counter and max_heap:
            maxi = -heapq.heappop(max_heap)

        mini = heapq.heappop(min_heap)
        while mini not in counter and min_heap:
            mini = heapq.heappop(min_heap)

        print(maxi, mini)


