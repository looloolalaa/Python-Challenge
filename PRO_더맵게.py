"""
heapq
"""
import heapq


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        new_taste = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, new_taste)
        count += 1

    return count


if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12], 7))