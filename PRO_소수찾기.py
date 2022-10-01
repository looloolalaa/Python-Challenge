# 에라토스테네스의 체 with set
def solution(n):
    primes = set(range(2, n+1))
    for i in range(2, int(n**0.5)+1):
        if i in primes:
            primes -= set(range(2*i, n+1, i))
    return len(primes)


if __name__ == '__main__':
    print(solution(10))