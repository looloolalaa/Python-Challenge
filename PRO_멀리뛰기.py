# [n] == [n-1] 에서 한칸 뛰기 + [n-2] 에서 두칸 뛰기
# => 피보나치
from math import factorial

def solution(n):
    result = 0
    two = 0
    while 2*two <= n:
        one = n - 2*two
        result += factorial(one + two) // (factorial(one) * factorial(two))
        two += 1
    return result % 1234567


if __name__ == '__main__':
    print(solution(4))