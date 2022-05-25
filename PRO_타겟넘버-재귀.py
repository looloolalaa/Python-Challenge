"""
solution 해석: numbers 에 +- 를 붙여서 target 을 만들수 있는 가짓수
== target+-numbers[0] 를 numbers[1:] 로 만들수 있는 가짓수
"""


def solution(numbers, target):
    if not numbers:
        return 1 if target == 0 else 0
    return solution(numbers[1:], target + numbers[0]) + solution(numbers[1:], target - numbers[0])


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))