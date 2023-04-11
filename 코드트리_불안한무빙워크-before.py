# 리스트 front 로 큐 구현
from collections import deque

n, k = map(int, input().split())
rail = list(map(int, input().split()))
people = deque([False for _ in range(n)])

length = 2*n

front = 0

def show():
    i = front
    for _ in range(length):
        print(rail[i], end=' ')
        i = (i+1) % length
    print()

def rotate():
    global front
    front = (front - 1 + length) % length

    people.pop()
    people.appendleft(False)

def down_person():
    if people[-1]:
        people[-1] = False


def go():
    for i in range(n-1, -1, -1):
        if people[i] and not people[i+1] and rail[(i+1+front) % length] != 0:
            rail[(i+1+front) % length] -= 1
            people[i+1] = True
            people[i] = False

def up_person():
    if not people[0] and rail[front] != 0:
        people[0] = True
        rail[front] -= 1

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


# simulate()
# simulate()
#
# rotate()
# go()
# down_person()
#
# show()
# print(people)

time = 0
while not is_done():
    simulate()
    time += 1
print(time)