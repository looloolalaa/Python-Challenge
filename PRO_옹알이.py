# 문자 한글자씩 비교
def solution(babbling):
    can = {"aya", "ye", "woo", "ma"}

    def isValid(s):
        while any(s.startswith(c) for c in can):
            for c in can:
                if s.startswith(c):
                    s = s[len(c):]
        return False if s else True

    result = 0
    for b in babbling:
        if isValid(b):
            result += 1
    return result


if __name__ == '__main__':
    print(solution(["aya", "yee", "u", "maa", "wyeoo"]))