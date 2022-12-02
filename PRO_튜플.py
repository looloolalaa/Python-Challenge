# split '},{'
def solution(s):
    s = s[2:-2].split('},{')
    s = [set()] + [set(c.split(',')) for c in s]
    s.sort(key=len)

    result = []
    for i in range(1, len(s)):
        result.append(int((s[i] - s[i - 1]).pop()))
    return result


if __name__ == '__main__':
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))