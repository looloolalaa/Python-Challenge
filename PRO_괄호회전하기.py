def solution(s):
    first = s
    result = 0
    for _ in range(len(s)):
        s = first[1:] + first[0]
        first = s
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        if not s:
            result += 1
    return result


if __name__ == '__main__':
    print(solution("[](){}"))