# 위에서 두 번째에 insert
# insert X => deque
from collections import deque

n = int(input())
tech = list(map(int, input().split()))

result = deque()

for i in range(n-1, -1, -1):
    card = n - i
    if tech[i] == 1:
        result.appendleft(card)
    if tech[i] == 2:
        top = result.popleft()
        result.appendleft(card)
        result.appendleft(top)
    if tech[i] == 3:
        result.append(card)

for r in result:
    print(r, end=' ')