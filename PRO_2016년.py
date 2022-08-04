"""
dictionary using list
"""


def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weeks = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    day = -1
    for m in range(a - 1):
        day += days[m]
    day += b

    return weeks[day % 7]


if __name__ == '__main__':
    print(solution(5, 24))