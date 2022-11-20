import heapq

# a little slow
def solution(cards):
    h = [0]
    for i in range(len(cards)):
        if cards[i] == 0:
            continue

        now, group = i, 0
        while cards[now] != 0:
            group += 1
            card = cards[now] - 1
            cards[now] = 0
            now = card
        heapq.heappush(h, -group)

    first = -heapq.heappop(h)
    second = -heapq.heappop(h)
    return first * second


if __name__ == '__main__':
    print(solution([8,6,3,7,2,5,1,4]))