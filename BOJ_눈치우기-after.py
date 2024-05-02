# 큰 값 두 개 계속 녹이기
import heapq

N = int(input())
h = []
res = 0
for s in map(int, input().split()):
    heapq.heappush(h, -s)

while len(h) > 1:
    a = -heapq.heappop(h)
    b = -heapq.heappop(h)

    res += b
    heapq.heappush(h, -(a-b))

res += -h[0]
print(-1 if res > 1440 else res)

