# 숫자 사이에 연산자 끼워넣기
from itertools import product

for _ in range(int(input())):
    N = int(input())

    a = [str(i) for i in range(1, N+1)]

    for ops in product([' ', '+', '-'], repeat=N-1):
        s = ''.join(''.join(z) for z in zip(a, ops)) + a[-1]
        if eval(s.replace(' ', '')) == 0:
            print(s)

    print()

