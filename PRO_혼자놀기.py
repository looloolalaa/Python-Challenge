# no heap -> two variable
def solution(cards):
    first, second = 0, 0
    for i in range(len(cards)):
        if cards[i] == 0:
            continue

        now, group = i, 0
        while cards[now] != 0:
            group += 1
            card = cards[now] - 1
            cards[now] = 0
            now = card

        if first < group:
            second = first
            first = group
        elif second < group:
            second = group

    return first * second


if __name__ == '__main__':
    print(solution([8,6,3,7,2,5,1,4]))