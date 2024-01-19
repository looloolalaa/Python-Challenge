# 최단 문자열 BFS
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    dp = ['x' for _ in range(10000)]

    A, B = map(int, input().split())
    dp[A] = ''
    que = deque([(A, '')])
    while que:
        n, d = que.popleft()
        D = n * 2 if n * 2 <= 9999 else n * 2 % 10000
        S = n - 1 if n != 0 else 9999
        strN = str(n).zfill(4)
        L = int(strN[1:] + strN[0])
        R = int(strN[-1] + strN[:-1])

        if dp[D] == 'x':
            dp[D] = d + 'D'
            if D == B:
                print(dp[B])
                continue
            que.append((D, dp[D]))
        if dp[S] == 'x':
            dp[S] = d + 'S'
            if S == B:
                print(dp[B])
                continue
            que.append((S, dp[S]))
        if dp[L] == 'x':
            dp[L] = d + 'L'
            if L == B:
                print(dp[B])
                continue
            que.append((L, dp[L]))
        if dp[R] == 'x':
            dp[R] = d + 'R'
            if R == B:
                print(dp[B])
                continue
            que.append((R, dp[R]))


    # print(dp[B])