# 데드라인 정렬 후 힙
import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[0], -x[1]))

h = []

for t, a in arr:
    if len(h) < t:
        heapq.heappush(h, a)
    elif h[0] < a:
        heapq.heappop(h)
        heapq.heappush(h, a)

print(sum(h))