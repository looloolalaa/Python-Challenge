# 이분 탐색
from itertools import combinations, product
from bisect import bisect_left


def solution(dice):
    n = len(dice)
    dice = [sorted(d) for d in dice]

    def win_rate(me, you):
        me_dice = [dice[m] for m in me]
        you_dice = [dice[y] for y in you]
        me_cases = sorted([sum(p) for p in product(*me_dice)])
        you_cases = sorted([sum(p) for p in product(*you_dice)])

        win_count = sum(bisect_left(you_cases, c) for c in me_cases)

        return win_count / len(me_cases) ** 2

    nums = set(i for i in range(n))
    result, maxi = -1, -1
    for me in combinations(nums, n // 2):
        you = tuple(nums - set(me))
        rate = win_rate(me, you)
        if maxi < rate:
            result = me
            maxi = rate

    return [r + 1 for r in result]