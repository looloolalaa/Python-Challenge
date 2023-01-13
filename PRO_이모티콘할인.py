# 구현 - 함수로 만들기
from itertools import product


def solution(users, emoticons):
    discount = [10, 20, 30, 40]
    candis = list(product(discount, repeat=len(emoticons)))

    aim = [0, 0]
    for can in candis:
        temp = []
        for d, p in users:
            buy = []
            for i, c in enumerate(can):
                if d <= c:
                    buy.append(i)
            temp.append(buy)

        total = []
        for t in temp:
            s = 0
            for b in t:
                s += emoticons[b] * (100 - can[b]) / 100
            total.append(s)

        sign, result = 0, 0
        for i in range(len(users)):
            if users[i][1] <= total[i]:
                sign += 1
            else:
                result += total[i]

        aim = max(aim, [sign, result])

    return aim


if __name__ == '__main__':
    print(solution([[40, 10000], [25, 10000]], [7000, 9000]))