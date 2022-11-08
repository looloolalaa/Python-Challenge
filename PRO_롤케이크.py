# len(Counter)
from collections import Counter


def solution(topping):
    left = Counter()
    right = Counter(topping)

    result = 0
    for t in topping:
        left[t] += 1
        right[t] -= 1
        if right[t] == 0:
            right.pop(t)

        if len(left) == len(right):
            result += 1

    return result


if __name__ == '__main__':
    print(solution([1, 2, 1, 3, 1, 4, 1, 2]))