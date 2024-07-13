# 두 수가 같을 때
from itertools import product
from math import gcd, lcm

gc, lc = map(int, input().split())
candi = []
for i in range(1, int(lc**0.5)+1):
    if lc % i == 0:
        candi.append(i)
        candi.append(lc//i)

ans, ans_sum = (-1, -1), float('inf')
for i, j in product(candi, repeat=2):
    if gc == gcd(i, j) and lc == lcm(i, j) and i+j < ans_sum:
        ans = i, j
        ans_sum = i+j

print(min(ans), max(ans))
