"""
약수
"""


def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            width, height = yellow // i, i
            if (width + height) * 2 + 4 == brown:
                return [width + 2, height + 2]

    return -1


if __name__ == '__main__':
    print(solution(8, 1))