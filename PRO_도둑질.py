"""
첫 번째 집을 털 경우, 마지막 집을 털 경우
a[i] = max(a[i-1], a[i-2] + money[i])
"""


def solution(money):
    a = [-1 for _ in range(len(money))]
    b = a.copy()
    a[0], a[1] = money[0], money[0]
    b[0], b[1] = 0, money[1]

    for i in range(2, len(a) - 1):
        a[i] = max(a[i - 1], a[i - 2] + money[i])

    for i in range(2, len(b)):
        b[i] = max(b[i - 1], b[i - 2] + money[i])

    return max(a[-2], b[-1])


if __name__ == '__main__':
    print(solution([1, 2, 3, 1]))