import heapq

N = int(input())
res = 0
if N == 1:
    res = int(input())
elif N == 2:
    a, b = map(int, input().split())
    res = max(a, b)
else:
    h = []
    for s in map(int, input().split()):
        heapq.heappush(h, -s)

    while h[0] != 0:
        a = -heapq.heappop(h)
        b = -heapq.heappop(h)
        c = -heapq.heappop(h)

        if a > b > c:
            dec = b - c
            res += dec

            heapq.heappush(h, -(a - dec))
            heapq.heappush(h, -(b - dec))
            heapq.heappush(h, -c)
        else:
            res += 1
            if b == 0:
                heapq.heappush(h, -(a - 1))
                heapq.heappush(h, -b)
                heapq.heappush(h, -c)
            else:
                heapq.heappush(h, -(a - 1))
                heapq.heappush(h, -(b - 1))
                heapq.heappush(h, -c)

print(-1 if res > 1440 else res)

