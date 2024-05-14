# que rotate
from collections import deque
import sys
sys.setrecursionlimit(10**6)

N, M, T = map(int, input().split())
arr = [deque(map(int, input().split())) for _ in range(N)]


def rotate(x, d, k):
    if d == 1:
        k *= -1
    for i in range(x-1, N, x):
        arr[i].rotate(k)

dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
def valid(i, j):
    return 0 <= i < N and 0 <= j < M


def dfs(i, j, n):
    for d in dxy:
        a, b = i+d[0], (j+d[1]+M)%M
        if valid(a, b) and arr[a][b] == n:
            arr[a][b] = 0
            dfs(a, b, n)


def erase():
    num = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                for d in dxy:
                    a, b = i + d[0], (j + d[1]+M)%M
                    if valid(a, b) and arr[a][b] == arr[i][j]:
                        num += 1
                        dfs(i, j, arr[i][j])
                        arr[i][j] = 0
                        break
    return num

def adjust():
    nums = [arr[i][j] for i in range(N) for j in range(M) if arr[i][j] != 0]
    if nums:
        avg = sum(nums) / len(nums)
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 0:
                    if arr[i][j] > avg:
                        arr[i][j] -= 1
                    elif arr[i][j] < avg:
                        arr[i][j] += 1

for _ in range(T):
    x, d, k = map(int, input().split())
    rotate(x, d, k)
    if erase() == 0:
        adjust()

print(sum(sum(a) for a in arr))
