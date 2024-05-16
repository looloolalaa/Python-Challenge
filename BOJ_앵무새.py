# 큐 제일 앞 매칭되면 삭제
from collections import deque

N = int(input())
ques = [deque(input().split()) for _ in range(N)]
L = deque(input().split())

while ques and L:
    target = L.popleft()
    for i in range(len(ques)):
        if ques[i][0] == target:
            ques[i].popleft()
            if not ques[i]:
                ques.pop(i)
            break

if not ques and not L:
    print('Possible')
else:
    print('Impossible')

