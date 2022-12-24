# 백준 큐2
from collections import deque
import sys

n = int(input())
q = deque()

result = []
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if s == 'pop':
        result.append(q.popleft() if q else -1)
    elif s == 'size':
        result.append(len(q))
    elif s == 'empty':
        result.append(1 if not q else 0)
    elif s == 'front':
        result.append(q[0] if q else -1)
    elif s == 'back':
        result.append(q[-1] if q else -1)
    else:
        _, x = s.split()
        q.append(x)

for r in result:
    print(r)