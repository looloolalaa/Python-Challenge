"""
DP - 점화식 먼저 세우기
i 번째 계단까지 올라오는 방법
[i-2] -> [i] or
[i-3] -> [i-1] -> [i]
"""
import sys

if __name__ == '__main__':
    N = int(input())
    stairs = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
    if N <= 2:
        print(sum(stairs))
        exit()

    a = [0 for _ in range(N)]
    a[0] = stairs[0]
    a[1] = stairs[0] + stairs[1]
    a[2] = max(stairs[0], stairs[1]) + stairs[2]

    for i in range(3, len(stairs)):
        a[i] = stairs[i] + max(a[i-2], a[i-3] + stairs[i-1])

    print(a[-1])