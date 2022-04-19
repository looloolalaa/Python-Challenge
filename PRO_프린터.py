"""
Queue
"""
from collections import deque


def solution(priorities, location):
    printed = []

    def get_max(l):
        result = -float('inf')
        for i, v in l:
            if v > result:
                result = v
        return result

    que = deque(list(enumerate(priorities)))
    while que:
        max_num = get_max(que)
        popped = que.popleft()
        if popped[1] == max_num:
            printed.append(popped)
        else:
            que.append(popped)

    for i, p in enumerate(printed):
        if location == p[0]:
            return i+1
    return -1