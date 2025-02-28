# 원차트에서 중심을 지나는 직선
from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))

def line_count(p):
    now = 0
    right, left = set(), set()
    for n in p:
        if now < 50:
            right.add(now)
        else:
            left.add(now - 50)
        now += n

    return len(left & right)

ans = 0
for p in permutations(arr, N):
    ans = max(ans, line_count(p))
print(ans)

