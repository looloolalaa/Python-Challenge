# 구간 큐 오름차순 유지
from collections import deque

N, L = map(int, input().split())
arr = list(map(int, input().split()))

que = deque()
for i in range(N):
    while que and que[-1][1] >= arr[i]:
        que.pop()

    if que and que[0][0] < i-L+1:
        que.popleft()

    que.append((i, arr[i]))
    print(que[0][1], end=' ')

