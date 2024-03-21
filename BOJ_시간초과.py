# 큰 수 가지치기
from math import factorial

C = int(input())
for _ in range(C):
    O, N, T, L = input().split()
    N, T, L = map(int, (N, T, L))
    limit = L * (10**8)
    time = -1
    if 'N!' in O:
        if N >= 13:
            print('TLE!')
            continue
        time = factorial(N) * T
    elif '2^N' in O:
        time = (2**N) * T
    elif 'N^3' in O:
        time = (N**3) * T
    elif 'N^2' in O:
        time = (N**2) * T
    else:
        time = N * T

    print('May Pass.' if time <= limit else 'TLE!')
