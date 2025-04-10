# 초밥 삭제 시점
from collections import defaultdict

L, Q = map(int, input().split())
foods = defaultdict(list)
people = {}

commands = []
for _ in range(Q):
    line = input().split()
    if line[0] == '100':
        t, x, name = int(line[1]), int(line[2]), line[3]
        commands.append([100, t, x, name])
        foods[name].append((t, x))
    elif line[0] == '200':
        t, x, name, n = int(line[1]), int(line[2]), line[3], int(line[4])
        commands.append([200, t, x, name, n])
        people[name] = [t, x, n]
    elif line[0] == '300':
        t = int(line[1])
        commands.append([300, t])

out_time = defaultdict(int)
for name in people:
    person = people[name]
    for food in foods[name]:
        if person[0] >= food[0]:  # 초밥 사람
            flow = person[0] - food[0]
            food_pos = (food[1] + flow) % L
            dist = person[1] - food_pos if person[1] >= food_pos else L - (food_pos - person[1])
            eat_time = person[0] + dist
        else:  # 사람 초밥
            dist = person[1] - food[1] if person[1] >= food[1] else L - (food[1] - person[1])
            eat_time = food[0] + dist

        commands.append([104, eat_time])
        out_time[name] = max(out_time[name], eat_time)

for name, time in out_time.items():
    commands.append([204, time])

commands.sort(key=lambda x: (x[1], x[0]))
a, b = 0, 0
for com in commands:
    if com[0] == 100:
        a += 1
    elif com[0] == 104:
        a -= 1
    elif com[0] == 200:
        b += 1
    elif com[0] == 204:
        b -= 1
    elif com[0] == 300:
        print(b, a)


