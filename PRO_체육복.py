"""
set
"""


def solution(n, lost, reserve):
    lost, reserve = set(lost), set(reserve)
    inter = lost & reserve
    lost -= inter
    reserve -= inter

    can = 0
    for l in lost:
        if l - 1 in reserve:
            can += 1
            reserve.remove(l - 1)
        elif l + 1 in reserve:
            can += 1
            reserve.remove(l + 1)

    return n - (len(lost) - can)


if __name__ == '__main__':
    print(solution(5, [2, 4], [1, 3, 5]))