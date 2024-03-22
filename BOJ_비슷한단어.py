# Counter 단어 차이
from collections import Counter

N = int(input())
s = input()
res = 0
for _ in range(N-1):
    a = input()
    x, y = (s, a) if len(s) >= len(a) else (a, s)
    cx, cy = Counter(x), Counter(y)
    if not cx - cy:
        res += 1
    elif len(cx - cy) == 1 and (cx-cy).popitem()[1] == 1:
        res += 1

print(res)

