# 투포인터 using queue
from collections import deque

def solution(n):
    result = 0
    que = deque([1])
    s = 1
    while que:
        if s == n:
            result += 1

        if s >= n:
            s -= que.popleft()
        else:
            new_num = que[-1] + 1
            que.append(new_num)
            s += new_num

    return result