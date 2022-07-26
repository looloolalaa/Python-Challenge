"""
basic N radix
"""


def solution(n):
    third = ''
    while n:
        third += str(n % 3)
        n //= 3

    answer = 0
    m = len(third) - 1
    for t in third:
        answer += int(t) * (3**m)
        m -= 1
    return answer


if __name__ == '__main__':
    print(solution(125))