# 3번 사용 => 4번 확인
import heapq
import sys
input = sys.stdin.readline

N, H, T = map(int, input().split())
h = []
for _ in range(N):
    heapq.heappush(h, -int(input()))


for t in range(T):
    if H > -h[0]:
        print('YES')
        print(t)
        exit(0)
    n = -heapq.heappop(h)
    nxt = n//2 if n != 1 else 1
    heapq.heappush(h, -nxt)

if H > -h[0]:
    print('YES')
    print(T)
else:
    print('NO')
    print(-h[0])
