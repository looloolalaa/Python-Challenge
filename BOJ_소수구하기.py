"""
에라토스테네스의 체
"""
if __name__ == '__main__':
    M, N = map(int, input().split())
    isPrime = [True for i in range(N+1)]
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2, int(N**0.5)+1):
        if isPrime[i]:
            j = i * 2
            while j <= N:
                isPrime[j] = False
                j += i


    for i in range(M, N+1):
        if isPrime[i]:
            print(i)
