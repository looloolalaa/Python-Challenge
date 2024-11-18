# 투 포인터(bisect)
from bisect import bisect_left, bisect_right

N = int(input())
A, B, C, D = [], [], [], []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab, cd = [], []
for i in range(N):
    for j in range(N):
        ab.append(A[i] + B[j])
        cd.append(C[i] + D[j])

ab.sort()
cd.sort()

ans = 0
start, end = 0, len(cd)-1
while start < len(ab) and end >= 0:
    s = ab[start] + cd[end]
    if s < 0:
        start += 1
    elif s > 0:
        end -= 1
    elif s == 0:
        start_right = bisect_right(ab, ab[start], start, len(ab))
        end_left = bisect_left(cd, cd[end], 0, end+1)

        ans += (start_right - start) * (end - end_left + 1)
        start = start_right
        end = end_left-1

print(ans)

