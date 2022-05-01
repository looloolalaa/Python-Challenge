"""
아무 것도 안입는 경우 len+1
아예 아무 것도 안입는 경우 -1
"""
from collections import defaultdict


def solution(clothes):
    book = defaultdict(list)
    for c, kind in clothes:
        book[kind].append(c)

    answer = 1
    for c in book.values():
        answer *= len(c) + 1
    return answer - 1


if __name__ == '__main__':
    print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))