# math.ceil
from collections import defaultdict
import math


def solution(fees, records):
    def time_to_num(t):
        h, m = t.split(':')
        return int(h) * 60 + int(m)

    in_time = {}
    total_time = defaultdict(int)
    for r in records:
        time, car, inout = r.split()
        if inout == 'IN':
            in_time[car] = time_to_num(time)
        if inout == 'OUT':
            total_time[car] += time_to_num(time) - in_time[car]
            in_time.pop(car)

    for car in in_time:
        total_time[car] += time_to_num('23:59') - in_time[car]

    cost = {}
    for car in total_time:
        if total_time[car] <= fees[0]:
            cost[car] = fees[1]
        else:
            cost[car] = fees[1] + math.ceil((total_time[car] - fees[0]) / fees[2]) * fees[3]

    return list(map(lambda x: x[1], sorted(cost.items(), key=lambda x: x[0])))


if __name__ == '__main__':
    print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))