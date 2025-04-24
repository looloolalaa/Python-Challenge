# 다익스트라 + 힙(재배열)
from collections import defaultdict
import heapq

Q = int(input())
line = list(map(int, input().split()))
n, m = line[1], line[2]
line = line[3:]
graph = defaultdict(list)
for i in range(0, 3 * m, 3):
    v, u, w = line[i], line[i + 1], line[i + 2]
    graph[v].append((u, w))
    if v != u:
        graph[u].append((v, w))

inf = float('inf')
dist = [inf for _ in range(n)]


def update_dist(start):
    for i in range(n):
        dist[i] = inf

    dist[start] = 0
    h = [(0, start)]
    while h:
        di, now = heapq.heappop(h)
        if dist[now] < di:
            continue

        for (a, ad) in graph[now]:
            new_di = dist[now] + ad
            if dist[a] > new_di:
                dist[a] = new_di
                heapq.heappush(h, (new_di, a))


update_dist(0)
products = {}
h = []
for _ in range(Q - 1):
    inp = list(map(int, input().split()))
    if inp[0] == 200:
        p_id, rev, dest = inp[1:]

        products[p_id] = (rev, dest)
        heapq.heappush(h, (-(rev - dist[dest]), p_id))

    elif inp[0] == 300:
        p_id = inp[1]

        if p_id in products:
            products.pop(p_id)

    elif inp[0] == 400:
        if not h:
            print(-1)
            continue

        point, p_id = h[0]
        if -point < 0:
            print(-1)
        else:
            target = -1
            temp = []
            while h:
                point, p_id = heapq.heappop(h)
                if p_id not in products:
                    continue

                if -point >= 0:
                    target = p_id
                    products.pop(target)
                    break
                temp.append((point, p_id))

            for t in temp:
                heapq.heappush(h, t)
            print(target)


    elif inp[0] == 500:
        s = inp[1]

        update_dist(s)
        new_h = []
        while h:
            _, p_id = heapq.heappop(h)
            if p_id not in products:
                continue

            rev, dest = products[p_id]
            heapq.heappush(new_h, (-(rev - dist[dest]), p_id))

        h = new_h

    # print(products)
    # print(h)
    # print(dist)
    # print()