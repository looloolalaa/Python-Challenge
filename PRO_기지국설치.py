"""
설치가 아직 안된 곳의 길이 divmod(d, 2*w+1)
몫 + 나머지
"""


def solution(n, stations, w):
    not_yet = []

    front = stations[0]-w-1
    if front > 0:
        not_yet.append(front)

    for i in range(len(stations)-1):
        between = stations[i+1]-w - (stations[i]+w) - 1
        if between > 0:
            not_yet.append(between)

    rear = n - (stations[-1]+w)
    if rear > 0:
        not_yet.append(rear)

    answer = 0
    for d in not_yet:
        answer += d // (2*w+1)
        if d % (2*w+1) != 0:
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution(11, [4, 11], 1))
