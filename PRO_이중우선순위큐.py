"""
min, max Heap
"""
import heapq


def solution(operations):
    min_h = []
    max_h = []

    for op in operations:
        o, n = op.split()
        if o == 'I':
            n = int(n)
            heapq.heappush(min_h, n)
            heapq.heappush(max_h, -n)
        elif o == 'D':
            if min_h:
                if n == '1':
                    maxi = -heapq.heappop(max_h)
                    min_h.remove(maxi)
                    heapq.heapify(min_h)
                elif n == '-1':
                    mini = heapq.heappop(min_h)
                    max_h.remove(-mini)
                    heapq.heapify(max_h)
                else:
                    print('error')
        else:
            print('error')

    if not min_h:
        return [0, 0]
    return [-max_h[0], min_h[0]]


if __name__ == '__main__':
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))