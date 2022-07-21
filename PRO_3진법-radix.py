"""
int N radix
"""


def solution(n):
    # 2, 8, 16 = bin(), oct(), hex()
    third = ''
    while n:
        third += str(n % 3)
        n //= 3

    # 10진수로 표현하되 base를 3으로
    return int(third, 3)


if __name__ == '__main__':
    print(solution(45))