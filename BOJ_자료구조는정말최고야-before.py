# O(NlogN): 스택 제일 위의 숫자로 최소힙
import heapq
import sys
input = sys.stdin.readline


h = []
N, M = map(int, input().split())
for _ in range(M):
    input()
    stack = list(map(int, input().split()))
    heapq.heappush(h, (stack[-1], stack))

i = 1
while h:
    top, stack = heapq.heappop(h)
    if top != i:
        print('No')
        exit(0)

    i += 1
    stack.pop()
    if stack:
        heapq.heappush(h, (stack[-1], stack))

print('Yes')