# Counter
from collections import Counter


def solution(want, number, discount):
    aim = {}
    for w, n in zip(want, number):
        aim[w] = n
    candis = Counter(discount[:10])

    result = 0
    if aim == candis:
        result += 1

    for i in range(10, len(discount)):
        candis[discount[i]] += 1
        poped = discount[i - 10]
        candis[poped] -= 1
        if candis[poped] == 0:
            candis.pop(poped)

        if aim == candis:
            result += 1

    return result


if __name__ == '__main__':
    print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))