# zip & append 삼항연산자
from collections import Counter


def solution(survey, choices):
    answer = ''
    total = Counter()
    for s, c in zip(survey, choices):
        if c < 4:
            total[s[0]] += 4 - c
        elif c > 4:
            total[s[1]] += c - 4

    answer += 'T' if total['R'] < total['T'] else 'R'
    answer += 'F' if total['C'] < total['F'] else 'C'
    answer += 'M' if total['J'] < total['M'] else 'J'
    answer += 'N' if total['A'] < total['N'] else 'A'
    return answer


if __name__ == '__main__':
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))