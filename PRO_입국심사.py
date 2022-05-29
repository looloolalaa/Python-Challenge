"""
[7, 10]
K초 동안 심사한 사람수: K//7 + K//10
"""


def solution(n, times):
    def total_people(t):
        return sum(t // time for time in times)

    start, end = 0, max(times) * n
    while start <= end:
        mid = (start + end) // 2
        if n <= total_people(mid):
            end = mid - 1
        else:
            start = mid + 1

    return start


if __name__ == '__main__':
    print(solution(6, [7, 10]))