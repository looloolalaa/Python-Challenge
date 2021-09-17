def time_to_int(time):
    time = time.split(':')
    return 60 * 60 * int(time[0]) + 60 * int(time[1]) + int(time[2])

def int_to_time(num):
    hour = str(num // 3600)
    minute = str((num % 3600) // 60)
    sec = str(num % 60)
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    if len(sec) == 1:
        sec = '0' + sec
    temp = [hour, minute, sec]
    return ':'.join(temp)

def solution(play_time, adv_time, logs):
    play_time = time_to_int(play_time)
    adv_time = time_to_int(adv_time)

    if play_time == adv_time:
        return "00:00:00"

    time_line = [0 for _ in range(play_time+1)]
    for log in logs:
        log = log.split('-')
        start = time_to_int(log[0])
        end = time_to_int(log[1])

        time_line[start] = time_line[start] + 1
        time_line[end] = time_line[end] - 1
    for i in range(1, len(time_line)):
        time_line[i] = time_line[i] + time_line[i-1]
    for i in range(1, len(time_line)):
        time_line[i] = time_line[i] + time_line[i - 1]

    max_time = 0
    answer = 0
    for i in range(0, play_time - adv_time + 1):
        if i == 0:
            total = time_line[i + adv_time - 1]
        else:
            total = time_line[i + adv_time - 1] - time_line[i - 1]
        if max_time < total:
            max_time = total
            answer = i

    return int_to_time(answer)


if __name__ == '__main__':
    play_time = "99:59:59"
    adv_time = "25:00:00"
    logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
    print(solution(play_time, adv_time, logs))
    keys = [1, 2, 3]
    values = ["A", "B", "C"]
    book = {}
    print([1,2,3])