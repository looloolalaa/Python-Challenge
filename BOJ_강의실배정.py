# 구간 그리디: 수업중인 강의실 중 가장 빨리
import heapq

arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr.sort()

h = [arr[0][1]]
for s, t in arr[1:]:
    fastest = h[0]
    if fastest <= s:
        heapq.heappop(h)
        heapq.heappush(h, t)
    else:
        heapq.heappush(h, t)

print(len(h))
