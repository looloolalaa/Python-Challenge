# 47금민수
from itertools import product
from bisect import bisect_left, bisect_right

a, b = map(int, input().split())

book = []
for d in range(1, 10):
    for p in product(['4', '7'], repeat=d):
        book.append(int(''.join(p)))

print(bisect_right(book, b) - bisect_left(book, a))

