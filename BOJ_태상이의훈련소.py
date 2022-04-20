"""
1차원 누적합
"""


import sys

N, M = map(int, input().split())
H = list(map(int, input().split()))

dx = [0 for _ in range(N+2)]

for _ in range(M):
    i, j, d = map(int, sys.stdin.readline().rstrip().split())
    dx[i] += d
    dx[j+1] -= d

for i in range(1, N+2):
    dx[i] += dx[i-1]

for i in range(N):
    H[i] += dx[i+1]

for h in H:
    print(h, end=' ')