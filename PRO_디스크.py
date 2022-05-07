"""
끝나는 시각 보다 앞에 있는(겹치는) 애들 중
가장 소요 시간이 짧은 task 를 선택.
가장 값이 작은 친구를 계속 뽑아야 하므로 'Heap'
"""
import heapq
from collections import deque


def solution(jobs):
    length = len(jobs)
    jobs = deque(sorted(jobs, key=lambda x: (x[0], x[1])))

    h = []
    task = jobs.popleft()
    heapq.heappush(h, (task[1], task[0]))

    time, total = 0, 0
    while h:
        take, start = heapq.heappop(h)
        time = max(time + take, start + take)
        total += time - start

        while jobs and jobs[0][0] < time:
            task = jobs.popleft()
            heapq.heappush(h, (task[1], task[0]))

        # 대기 task 는 없는데 jobs 이 남아 있을 때
        if not h and jobs:
            task = jobs.popleft()
            time = task[0]
            heapq.heappush(h, (task[1], task[0]))

    return total // length


if __name__ == '__main__':
    print(solution([[0, 3], [1, 9], [2, 6]]))