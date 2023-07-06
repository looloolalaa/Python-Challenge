# replace('aya', '*')
# replace('aya', '') 로 쓰면 문제가 있으미
def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    cant = ["ayaaya", "yeye", "woowoo", "mama"]

    result = 0
    for b in babbling:
        if any(t in b for t in cant):
            continue

        for c in can:
            b = b.replace(c, '*')

        if all(ch == '*' for ch in b):
            result += 1

    return result
