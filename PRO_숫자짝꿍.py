# Counter 교집합(&)
# int(큰수) -> 시간초과
from collections import Counter


def solution(X, Y):
    inter = Counter(X) & Counter(Y)
    if not inter:
        return "-1"

    result = ''
    for num, count in sorted(inter.items(), key=lambda x: -int(x[0])):
        result += num * count
    return "0" if all(r == "0" for r in result) else result