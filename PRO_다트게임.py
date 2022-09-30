# string traversal
def solution(dartResult):
    score = []
    dartResult = dartResult.replace('10', 't')
    for c in dartResult:
        if c == 't':
            score.append(10)
        if '0' <= c <= '9':
            score.append(int(c))
        if c == 'D':
            score[-1] **= 2
        if c == 'T':
            score[-1] **= 3
        if c == '*':
            score[-1] *= 2
            if len(score) >= 2:
                score[-2] *= 2
        if c == '#':
            score[-1] *= -1
    return sum(score)


if __name__ == '__main__':
    print(solution('1D2S#10S'))