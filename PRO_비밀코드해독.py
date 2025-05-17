# 숫자야구게임
from itertools import combinations


def solution(n, q, ans):
    # print(bin(7)[2:].count('1'))

    def to_int(nums):
        res = 0
        for n in nums:
            res |= (1 << n)
        return res

    q = [to_int(nums) for nums in q]
    result = 0
    for com in combinations(range(1, n + 1), 5):
        standard = to_int(com)

        for num, cnt in zip(q, ans):
            if bin(standard & num)[2:].count('1') != cnt:
                break
        else:
            result += 1

    return result