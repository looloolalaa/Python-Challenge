# 큐 돌리기
from collections import deque
N, M, R = map(int, input().split())
arr = [input().split() for _ in range(N)]

ques = []
n, m = N, M
left, top = 0, 0
for _ in range(min(N, M)//2):
    que = deque()
    i, j = left, top
    for _ in range(n-1):
        que.append(arr[i][j])
        i += 1
    for _ in range(m-1):
        que.append(arr[i][j])
        j += 1
    for _ in range(n-1):
        que.append(arr[i][j])
        i -= 1
    for _ in range(m-1):
        que.append(arr[i][j])
        j -= 1

    ques.append(que)

    left += 1
    top += 1
    n -= 2
    m -= 2

for _ in range(R):
    for que in ques:
        que.appendleft(que.pop())

res = [[-1 for _ in range(M)] for _ in range(N)]
n, m = N, M
left, top = 0, 0
for k in range(min(N, M)//2):
    que = ques[k]
    i, j = left, top
    for _ in range(n-1):
        res[i][j] = que.popleft()
        i += 1
    for _ in range(m-1):
        res[i][j] = que.popleft()
        j += 1
    for _ in range(n-1):
        res[i][j] = que.popleft()
        i -= 1
    for _ in range(m-1):
        res[i][j] = que.popleft()
        j -= 1

    left += 1
    top += 1
    n -= 2
    m -= 2


for r in res:
    print(*r)