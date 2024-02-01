# 최대 값 갱신
from collections import deque
import heapq


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    que = deque(enumerate(arr))
    h = []
    for a in arr:
        heapq.heappush(h, -a)


    while que:
        i, n = que.popleft()
        maxi = -h[0]

        if n < maxi:
            que.append((i, n))
            continue
        elif n == maxi:
            heapq.heappop(h)
            if i == M:
                break

    print(len(arr) - len(que))

