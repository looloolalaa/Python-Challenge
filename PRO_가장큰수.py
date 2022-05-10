"""
자릿수 비교
'3' '30' -> '3333' '3030'
"""


def solution(numbers):
    def repeat(n):
        a = n * 4
        return a[0], a[1], a[2], a[3]

    numbers = list(map(str, numbers))
    numbers.sort(key=repeat, reverse=True)
    if numbers[0] == '0':
        return '0'
    return ''.join(numbers)


if __name__ == '__main__':
    print(solution([3, 30, 34, 5, 9]))