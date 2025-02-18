# 두 벡터의 외적으로 시계 반시계 판별
# (x1,y1) x (x2,y2) == x1*y2 - y1*x2
# 외적 값 기준: 0
from itertools import permutations

arr = list(map(int, input().split()))

def isInner(a, b, c):
    ba = [a[0] - b[0], a[1] - b[1]]
    bc = [c[0] - b[0], c[1] - b[1]]

    outer = ba[0] * bc[1] - ba[1] * bc[0]
    return outer >= 0

r = 1/(2**0.5)
directs = [[0,1], [r,r], [1,0], [r,-r], [0,-1], [-r,-r], [-1,0], [-r,r]]
def valid(p):
    points = [[di[0]*dist, di[1]*dist] for di, dist in zip(directs, p)]
    for i in range(8):
        if not isInner(points[i-1], points[i], points[(i+1)%8]):
            return False
    return True

ans = 0
for p in permutations(arr, 8):
    if valid(p):
        ans += 1
print(ans)

