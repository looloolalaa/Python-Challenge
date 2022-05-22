"""
K개로 만들 수 있는 숫자들
== (N*K) + ({1개} op {K-1}) + ({2개} op {K-2}) + ..

set(4)
== NNNN + (1 op 3) + (2 op 2) + (3 op 1)
"""
from collections import defaultdict


# DP
def solution(N, number):
    book = defaultdict(set)
    # 길이 l 로 만들 수 있는 숫자들

    def calc(x, y):
        x, y = book[x], book[y]
        ret_set = set()
        for i in x:
            for j in y:
                ret_set.update({i + j, i * j, i - j, j - i})
                if j != 0:
                    ret_set.add(i // j)
                if i != 0:
                    ret_set.add(j // i)

        return ret_set

    for l in range(1, 9):
        book[l].add(int(str(N) * l))
        for a in range(1, l // 2 + 1):
            b = l - a
            book[l].update(calc(a, b))

        if number in book[l]:
            return l

    # print(book[1], book[3])
    return -1


if __name__ == '__main__':
    print(solution(5, 12))