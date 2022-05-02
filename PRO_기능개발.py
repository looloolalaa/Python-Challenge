"""
One loop
while time[i] > date:
"""


def solution(progresses, speeds):
    time = []

    for p, s in zip(progresses, speeds):
        remain = 100 - p
        take = remain // s
        if remain % s > 0:
            take += 1
        time.append(take)

    count = 1
    result = []
    # time = [20,1,1,20, 30]
    date = time[0]
    for i in range(1, len(time)):
        if date < time[i]:
            result.append(count)
            count = 1
            date = time[i]
        else:
            count += 1
    result.append(count)
    return result


if __name__ == '__main__':
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))