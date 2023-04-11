# 1차원 배열 회전 => Queue
from collections import deque

n, k = map(int, input().split())
rail = deque(list(map(int, input().split())))
people = deque([False for _ in range(n)])

def rotate():
    rail.appendleft(rail.pop())
    people.pop()
    people.appendleft(False)

def down_person():
    if people[-1]:
        people[-1] = False


def go():
    for i in range(n-1, -1, -1):
        if people[i] and not people[i+1] and rail[i+1] != 0:
            rail[i+1] -= 1
            people[i+1] = True
            people[i] = False

def up_person():
    if not people[0] and rail[0] != 0:
        people[0] = True
        rail[0] -= 1

def is_done():
    count = 0
    for r in rail:
        if r == 0:
            count += 1
    return count >= k

def simulate():
    rotate()
    down_person()

    go()
    down_person()

    up_person()
    down_person()

time = 0
while not is_done():
    simulate()
    time += 1
print(time)