# 먼저 풀어야 하는 문제 번호
import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = {i+1 for i in range(N)}
behind = defaultdict(list)
front = defaultdict(int)

for _ in range(M):
    A, B = map(int, input().split())
    behind[A].append(B)
    front[B] += 1
    if B in nums:
        nums.remove(B)


h = []
for n in nums:
    heapq.heappush(h, n)


visited = [False for _ in range(N+1)]
while h:
    num = heapq.heappop(h)
    if visited[num]:
        continue

    print(num, end=' ')
    visited[num] = True

    while behind[num]:
        b = behind[num].pop()
        front[b] -= 1
        if front[b] == 0:
            heapq.heappush(h, b)

