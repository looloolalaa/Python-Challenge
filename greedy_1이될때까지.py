if __name__ == '__main__':
    N, K = map(int, input().split())
    count = 0
    while N > 1:
        if N >= K and N % K == 0:
            N //= K
            count += 1
        else:
            count += N % K
            N = N - (N%K)

    print(count)