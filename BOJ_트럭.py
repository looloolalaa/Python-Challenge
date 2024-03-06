from collections import deque

n, w, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))

que = deque([0 for _ in range(w)])
s = 0
time = 0
while trucks:
    s -= que.popleft()
    if s + trucks[0] <= L:
        truck = trucks.popleft()
        que.append(truck)
        s += truck
    else:
        que.append(0)

    time += 1

print(time + w)