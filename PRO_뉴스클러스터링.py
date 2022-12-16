# 중복집합
from collections import Counter


def solution(str1, str2):
    c1, c2 = Counter(), Counter()
    keys = set()

    for i in range(len(str1) - 1):
        s = str1[i] + str1[i + 1]
        if s.isalpha():
            s = s.upper()
            c1[s] += 1
            keys.add(s)

    for i in range(len(str2) - 1):
        s = str2[i] + str2[i + 1]
        if s.isalpha():
            s = s.upper()
            c2[s] += 1
            keys.add(s)

    if not c1 and not c2:
        return 65536

    inter, union = 0, 0
    for key in keys:
        inter += min(c1[key], c2[key])
        union += max(c1[key], c2[key])

    return int(inter / union * 65536)


if __name__ == '__main__':
    print(solution('FRANCE', 'french'))