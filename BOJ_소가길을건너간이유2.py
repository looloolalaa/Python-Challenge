# ABCBCA
from collections import defaultdict

book = defaultdict(list)
s = input()
for i in range(52):
    book[s[i]].append(i)


res = 0
for i, a in book.items():
    for j, b in book.items():
        if a[0] < b[0] < a[1] < b[1]:
            res += 1

print(res)