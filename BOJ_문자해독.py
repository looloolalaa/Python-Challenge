# swiping window
from collections import Counter

n, m = map(int, input().split())
a = input()
b = input()

x = Counter(a)
y = Counter(b[:n])

count = 0
if x == y:
    count += 1

for i in range(m - n):
    y[b[i]] -= 1
    if y[b[i]] == 0:
        y.pop(b[i])
    y[b[i + n]] += 1

    if x == y:
        count += 1

print(count)
