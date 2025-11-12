import requests
import json
import random

base_url = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users/'
x_auth_token = 'f0016f0c44d17eb674b3ec2f9da1165b'


def get_auth_key(problem_num, x_auth):
    x_header = {'X-Auth-Token': x_auth_token, 'Content-Type': 'application/json'}
    x_param = {'problem': problem_num}
    response = requests.post(url=base_url + 'start', headers=x_header, data=json.dumps(x_param))
    return response.json()['auth_key']


def get_pos(loc_id):
    return n - 1 - loc_id % n, loc_id // n


def get_locations():
    response = requests.get(url=base_url + 'locations', headers=header)
    locations = response.json()['locations']
    for loc in locations:
        loc_id, c = loc['id'], loc['located_bikes_count']
        i, j = get_pos(loc_id)
        table[i][j] = c


def get_trucks():
    response = requests.get(url=base_url + 'trucks', headers=header)
    for line in response.json()['trucks']:
        tid, loc_id = line['id'], line['location_id']
        trucks[tid] = get_pos(loc_id)


dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dxy += [(0, 2), (2, 0), (0, -2), (-2, 0)]
dxy += [(1, 1), (1, -1), (-1, -1), (-1, 1)]
dxy += [(0, 3), (1, 2), (2, 1), (3, 0), (2, -1), (1, -2), (0, -3), (-1, -2), (-2, -1), (0, -3), (-2, 1), (-1, 2)]


def is_valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


def find_nearest_truck(p):
    min_dis = float('inf')
    min_truck_id = -1
    for tid in trucks:
        t_pos = trucks[tid]
        dis = abs(p[0] - t_pos[0]) + abs(p[1] - t_pos[1])
        if min_dis > dis:
            min_dis = dis
            min_truck_id = tid
    return min_truck_id


# (-2, 1)
def get_moves(move):
    result = []
    if move[0] != 0:
        for _ in range(abs(move[0])):
            result.append(1 if move[0] < 0 else 3)
    if move[1] != 0:
        for _ in range(abs(move[1])):
            result.append(4 if move[1] < 0 else 2)
    return result



def get_send():
    send = []
    for i in range(n):
        for j in range(n):
            now_bike = table[i][j]
            for d in dxy:
                a = i + d[0], j + d[1]
                if is_valid(a):
                    diff = now_bike - table[a[0]][a[1]]
                    if diff >= 2:
                        send.append(((i, j), a))
                        table[i][j] -= 1
                        table[a[0]][a[1]] += 1
                        break

    # [((1, 2),(3, 4)), ((0, 0), (4, 1))]
    return send


def simulate1():
    send = get_send()
    commands = []
    for s in send:
        if not trucks:
            break
        start, end = s[0], s[1]
        truck_id = find_nearest_truck(start)
        truck_pos = trucks[truck_id]
        trucks.pop(truck_id)

        order = []

        # truck -> start
        i_move, j_move = start[0] - truck_pos[0], start[1] - truck_pos[1]
        moves_to_start = get_moves((i_move, j_move))
        order += moves_to_start

        # up 1
        order.append(5)

        # start -> end
        i_move, j_move = end[0] - start[0], end[1] - start[1]
        order += get_moves((i_move, j_move))

        # down 1
        order.append(6)

        if len(order) > 10:
            order = moves_to_start[:10]

        command = {'truck_id': truck_id, 'command': order}
        commands.append(command)



    # print(send)
    # print(commands)


    data = {'commands': commands}
    response = requests.put(url=base_url + 'simulate', headers=header, data=json.dumps(data))
    response = response.json()
    print(response)


temp = [[1, 2], [2, 3], [3, 4], [4, 1]]
pattern = 0
hot_places = [[3037, 3386], [2635], [2465]]
cool_places = [[3595], [628, 724], [969, 3515]]


def get_dis(start_id, end_id):
    s, e = get_pos(start_id), get_pos(end_id)
    return abs(s[0] - e[0]) + abs(s[1] - e[1])


def simulate2():
    # print(trucks)
    global pattern
    commands = []

    hot_cool_places = hot_places[pattern] + cool_places[pattern]
    hot_cool_places.reverse()

    for tid in trucks:
        t_pos = trucks[tid]
        around = [t_pos]
        for d in dxy:
            a = t_pos[0] + d[0], t_pos[1] + d[1]
            if is_valid(a):
                around.append(a)

        max_pos = max(around, key=lambda x: table[x[0]][x[1]])
        min_pos = min(around, key=lambda x: table[x[0]][x[1]])
        diff = table[max_pos[0]][max_pos[1]] - table[min_pos[0]][min_pos[1]]
        order = []
        if diff < 2:
            if hot_cool_places:
                hc_id = hot_cool_places.pop()
                hot_place = get_pos(hc_id)

                # truck -> hot place
                i_move, j_move = hot_place[0] - t_pos[0], hot_place[1] - t_pos[1]
                order += get_moves((i_move, j_move))[:10]

            else:
                random_move = temp[random.randint(0, 3)]
                for _ in range(5):
                    order += random_move
        else:
            # truck -> max_pos
            i_move, j_move = max_pos[0] - t_pos[0], max_pos[1] - t_pos[1]
            moves_to_start = get_moves((i_move, j_move))
            order += moves_to_start.copy()

            take = diff // 2
            if take > 3:
                take = 3

            # up (take)
            for _ in range(take):
                order.append(5)

            # max_pos -> min_pos
            i_move, j_move = min_pos[0] - max_pos[0], min_pos[1] - max_pos[1]
            order += get_moves((i_move, j_move))

            # down (take)
            for _ in range(take):
                order.append(6)

            # order = [1,1,2,2,5,4,6]
            if len(order) > 10:
                order = moves_to_start[:10]
            else:
                table[max_pos[0]][max_pos[1]] -= take
                table[min_pos[0]][min_pos[1]] += take

        command = {'truck_id': tid, 'command': order}
        commands.append(command)

    # print(commands)

    data = {'commands': commands}
    response = requests.put(url=base_url + 'simulate', headers=header, data=json.dumps(data))
    response = response.json()
    print(response)

    if (int(response['time']) + 1) % 240 == 0:
        pattern += 1
        if pattern > 2:
            pattern = 2




def get_score():
    response = requests.get(url=base_url + 'score', headers=header)
    return response.json()['score']


pid = 2
auth_key = get_auth_key(pid, x_auth_token)
# auth_key = 'a63e5193-c357-48b8-b09d-80b1278fcf9a'
header = {'Authorization': auth_key, 'Content-Type': 'application/json'}

if __name__ == '__main__':
    n, bike, truck = (5, 4, 5) if pid == 1 else (60, 3, 10)

    table = [[0 for _ in range(n)] for _ in range(n)]
    trucks = {}

    while get_score() == 0:
        get_locations()
        get_trucks()

        # for t in table:
        #     print(t)

        if pid == 1:
            simulate1()
        else:
            simulate2()

    print(get_score())
