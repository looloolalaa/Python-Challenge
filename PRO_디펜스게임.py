# 지금까지 저장된 값중 가장 큰 값 필요: heap
import heapq


def solution(n, k, enemy):
    h = []
    for r in range(len(enemy)):
        heapq.heappush(h, -enemy[r])
        n -= enemy[r]
        if n < 0:
            if k > 0:
                n += -heapq.heappop(h)
                k -= 1
            else:
                return r

    return len(enemy)


if __name__ == '__main__':
    print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))