# 노드 추가 시, 최대 깊이 제한
# 서브트리 색깔 바꾸기
from collections import defaultdict

Q = int(input())
parent = {}
color = {}
max_depth = {}
last_update = {-1: -1}
children = defaultdict(list)


def insert(a, b, c, d, t):
    parent[a] = b
    color[a] = c
    max_depth[a] = d
    last_update[a] = t
    children[b].append(a)


def try_insert(a, b, c, d, t):
    if b == -1:
        insert(a, b, c, d, t)
        return

    new_depth = 2
    now = b
    while now != -1:
        if new_depth > max_depth[now]:
            return
        now = parent[now]
        new_depth += 1

    insert(a, b, c, d, t)


def change_color(a, c, t):
    color[a] = c
    last_update[a] = t


def get_color(a):
    now = a
    lastest_time = -1
    last_color = -1
    while now != -1:
        if last_update[now] > lastest_time:
            lastest_time = last_update[now]
            last_color = color[now]
        now = parent[now]

    return last_color


def update_color(node):
    now = last_update[node]
    for child in children[node]:
        if last_update[child] < now:
            last_update[child] = now
            color[child] = color[node]
        update_color(child)


def get_total_score():
    update_color(-1)
    ans = 0

    def diff_color_set(node):
        nonlocal ans

        color_set = set() if node == -1 else {color[node]}
        for child in children[node]:
            color_set |= diff_color_set(child)

        ans += len(color_set) ** 2 if node != -1 else 0
        return color_set

    diff_color_set(-1)
    return ans


for time in range(Q):
    inp = list(map(int, input().split()))
    com = inp[0]
    if com == 100:
        a, b, c, d = inp[1:]
        try_insert(a, b, c, d, time)
    elif com == 200:
        a, c = inp[1:]
        change_color(a, c, time)
    elif com == 300:
        a = inp[1]
        print(get_color(a))
    elif com == 400:
        print(get_total_score())


# == parent만 확인하기 (+시점)
