# 문자열 valid
from itertools import combinations

L, C = map(int, input().split())
s = sorted(input().split())

mo = 'aeiou'
def valid(s):
    x, y = 0, 0
    for c in s:
        if c in mo:
            x += 1
        else:
            y += 1
    return x >= 1 and y >= 2

for candi in combinations(s, L):
    if valid(candi):
        print(''.join(candi))
