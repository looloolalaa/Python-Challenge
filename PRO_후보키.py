# db candidate key
from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    def valid(com):
        s = set()
        for r in relation:
            added = ''
            for i in com:
                added += r[i]
            s.add(added)
        return len(s) == row

    candis = []
    temp = [i for i in range(col)]
    for l in range(1, col + 1):
        candis += list(combinations(temp, l))

    result = []
    for c in candis:
        # 최소성 and 유일성 순서 꽤 중요
        if all(not (r < set(c)) for r in result) and valid(c):
            result.append(set(c))

    return len(result)


if __name__ == '__main__':
    print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))