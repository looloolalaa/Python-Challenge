"""
dp[i] == array[i]로 끝나는 애들 개수 j: [0~i-1]
그 최장 문자열 == [n-1~0] 역탐색
"""


if __name__ == '__main__':
    N = int(input())
    array = list(map(int, input().split()))

    dp = [1 for _ in range(N)]
    for i in range(1, N):
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_len = max(dp)
    x = max_len

    seq = []
    for i in reversed(range(N)):
        if dp[i] == x:
            seq.append(array[i])
            x -= 1
    seq.reverse()

    print(max_len)
    for s in seq:
        print(s, end=' ')