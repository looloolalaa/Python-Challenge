# greedy - 4n
from collections import deque


def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)

    for i in range(len(queue1) * 4):
        if sum1 == sum2:
            return i
        if sum1 > sum2:
            queue1, queue2 = queue2, queue1
            sum1, sum2 = sum2, sum1

        poped = queue2.popleft()
        queue1.append(poped)
        sum2 -= poped
        sum1 += poped

    return -1


if __name__ == '__main__':
    print(solution([1, 2, 1, 2], [1, 10, 1, 2]))