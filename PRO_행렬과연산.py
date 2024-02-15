# 행렬 테두리 덱
from collections import deque


def solution(rc, operations):
    r, c = len(rc), len(rc[0])

    top, bottom = deque(rc[0]), deque(rc[-1])
    left = deque([rc[i][0] for i in range(r)])
    right = deque([rc[i][-1] for i in range(r)])
    rc = deque(deque(r) for r in rc)

    for op in operations:
        if op == 'ShiftRow':
            left.appendleft(left.pop())
            right.appendleft(right.pop())
            rc.pop()
            rc.appendleft(bottom)
            top, bottom = rc[0], rc[-1]
            bottom[0], bottom[-1] = left[-1], right[-1]
            top[0], top[-1] = left[0], right[0]
            rc[0], rc[-1] = top, bottom

        elif op == 'Rotate':
            top.appendleft(left[1])
            top.pop()
            right.appendleft(top[-1])
            right.pop()
            bottom.append(right[-1])
            bottom.popleft()
            left.append(bottom[0])
            left.popleft()
            rc[0], rc[-1] = top, bottom

    res = [list(top)]
    for i in range(1, r - 1):
        res.append([left[i]] + [rc[i][j] for j in range(1, c - 1)] + [right[i]])
    res.append(list(bottom))

    return res