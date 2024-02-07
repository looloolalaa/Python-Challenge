import sys
import heapq
input = sys.stdin.readline

h = []
N = int(input())
for _ in range(N):
    q = int(input())
    if q != 0:
        heapq.heappush(h, q)
    else:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h))