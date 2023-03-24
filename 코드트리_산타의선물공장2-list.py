# 더블링크드 리스트 배열 구현
from math import floor

q = int(input())
first_line = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(q - 1)]

n, m = first_line[1], first_line[2]
belt_pos = first_line[3:]

# belts
head, tail, count = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
# boxes
prv, nxt = [0 for _ in range(m + 1)], [0 for _ in range(m + 1)]


def append_box(belt, box):
    if box == 0:
        return

    if count[belt] == 0:
        head[belt] = tail[belt] = box
        count[belt] = 1
    else:
        origin_tail = tail[belt]
        tail[belt] = box
        prv[box] = origin_tail
        nxt[origin_tail] = box
        count[belt] += 1


def prepend_box(belt, box):
    if box == 0:
        return

    if count[belt] == 0:
        head[belt] = tail[belt] = box
        count[belt] = 1
    else:
        origin_head = head[belt]
        head[belt] = box
        nxt[box] = origin_head
        prv[origin_head] = box
        count[belt] += 1


def pop_head(belt):
    if count[belt] == 0:
        return 0

    if count[belt] == 1:
        popped = head[belt]
        head[belt] = tail[belt] = 0
        count[belt] = 0
        return popped

    popped = head[belt]
    head[belt] = nxt[popped]

    nxt[popped] = prv[head[belt]] = 0
    count[belt] -= 1
    return popped


def move_all(belt_a, belt_b):
    if count[belt_a] == 0:
        return count[belt_b]

    if count[belt_b] == 0:
        head[belt_b] = head[belt_a]
        tail[belt_b] = tail[belt_a]
    else:
        tail_a, head_b = tail[belt_a], head[belt_b]
        head[belt_b] = head[belt_a]

        nxt[tail_a] = head_b
        prv[head_b] = tail_a

    head[belt_a] = tail[belt_a] = 0
    count[belt_b] += count[belt_a]
    count[belt_a] = 0
    return count[belt_b]


def change_front(belt_a, belt_b):
    popped_a, popped_b = pop_head(belt_a), pop_head(belt_b)
    prepend_box(belt_b, popped_a)
    prepend_box(belt_a, popped_b)
    return count[belt_b]


def divide(belt_a, belt_b):
    temp = []
    for _ in range(floor(count[belt_a] / 2)):
        temp.append(pop_head(belt_a))

    while temp:
        t = temp.pop()
        prepend_box(belt_b, t)

    return count[belt_b]


def get_box_info(box):
    a = prv[box] if prv[box] != 0 else -1
    b = nxt[box] if nxt[box] != 0 else -1
    return a + 2 * b


def get_belt_info(belt):
    a = head[belt] if head[belt] != 0 else -1
    b = tail[belt] if tail[belt] != 0 else -1
    c = count[belt]
    return a + 2 * b + 3 * c


def show():
    for i in range(1, n + 1):
        p = head[i]
        while p != 0:
            print(p, end=' ')
            p = nxt[p]
        print(':', count[i])


for box in range(m):
    append_box(belt_pos[box], box + 1)

# move_all(2, 4)
# change_front(4, 2)
# divide(4, 2)
# get_box_info(6)
# get_box_info(5)
# get_belt_info(1)
# get_belt_info(3)
# show()


result = []
for q in query:
    if q[0] == 200:
        m_src, m_dst = q[1], q[2]
        res = move_all(m_src, m_dst)
        result.append(res)
    elif q[0] == 300:
        m_src, m_dst = q[1], q[2]
        res = change_front(m_src, m_dst)
        result.append(res)
    elif q[0] == 400:
        m_src, m_dst = q[1], q[2]
        res = divide(m_src, m_dst)
        result.append(res)
    elif q[0] == 500:
        p_num = q[1]
        res = get_box_info(p_num)
        result.append(res)
    elif q[0] == 600:
        b_num = q[1]
        res = get_belt_info(b_num)
        result.append(res)

for r in result:
    print(r)