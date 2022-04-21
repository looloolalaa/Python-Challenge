"""
Greedy
"""


def solution(d, budget):
    d.sort()

    for i, a in enumerate(d):
        if a <= budget:
            budget -= a
        else:
            break
    else:
        i += 1
    return i