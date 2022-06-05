"""
가장 큰 work를 계속 찾아야 하므로 Heap
"""
import heapq


def solution(n, works):
    h = []
    for work in works:
        heapq.heappush(h, -work)

    while n > 0:
        big = heapq.heappop(h)
        if big == 0:
            return 0
        big += 1
        n -= 1
        heapq.heappush(h, big)

    return sum(w ** 2 for w in h)


if __name__ == '__main__':
    print(solution(4, [4, 3, 3]))