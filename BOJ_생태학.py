# 입력(EOF) + 소수점반올림: round X
from collections import Counter
import sys

N = 0
counter = Counter()
while name := sys.stdin.readline().rstrip():
    counter[name] += 1
    N += 1

for k, v in sorted(counter.items(), key=lambda x: x[0]):
    print('{} {:.4f}'.format(k, v/N*100))
