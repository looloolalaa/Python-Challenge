# Queue
from collections import deque


def solution(cards1, cards2, goal):
    cards1, cards2, goal = deque(cards1), deque(cards2), deque(goal)
    while goal:
        target = goal[0]
        if cards1 and target == cards1[0]:
            cards1.popleft()
        elif cards2 and target == cards2[0]:
            cards2.popleft()
        else:
            return 'No'
        goal.popleft()
    return 'Yes'


if __name__ == '__main__':

    print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))