# 1사분면 직선방정식의 윗 범위로 세 점 180도 검증
# using xy절편(길이) 좌표X
from itertools import permutations

arr = list(map(int, input().split()))

def valid(a, b, c):
    # y == (-a/c)*x + a
    x, y = (b/(2**0.5), b/(2**0.5))
    return y >= (-a / c) * x + a

def valid_shape(p):
    for i in range(8):
        if not valid(p[i], p[(i+1) % 8], p[(i+2) % 8]):
            return False
    return True

ans = 0
for p in permutations(arr, 8):
    if valid_shape(p):
        ans += 1
print(ans)