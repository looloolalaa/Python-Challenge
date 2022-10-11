# 16진수 돌리기
from collections import deque

answer = []
T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    s = deque(input())

    m = n // 4
    candis = set()

    for _ in range(m):
        for i in range(4):
            candis.add(''.join(list(s)[i * m: i * m + m]))
        s.append(s.popleft())

    candis = [int(c, 16) for c in candis]
    answer.append(sorted(candis, reverse=True)[k - 1])

for i in range(len(answer)):
    print('#{0} {1}'.format(i + 1, answer[i]))