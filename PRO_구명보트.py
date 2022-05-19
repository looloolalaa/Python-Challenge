"""
limit 에 최대한 가깝게 보트 태우기
i  .. <-j 이동
"""


def solution(people, limit):
    boat = 0
    people.sort()

    a, b = 0, len(people) - 1
    while a < b:
        if people[a] + people[b] <= limit:
            boat += 1
            a += 1
        b -= 1

    return len(people) - boat


if __name__ == '__main__':
    print(solution([70, 50, 80, 50], 100))