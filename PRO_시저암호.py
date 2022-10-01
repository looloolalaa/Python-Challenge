# ord & chr
def solution(s, n):
    result = ''
    for c in s:
        if c == ' ':
            result += ' '
        else:
            p = chr(ord(c) + n)
            if c.isupper():
                result += chr(ord('A') + (ord(p) - ord('A'))%26)
            if c.islower():
                result += chr(ord('a') + (ord(p) - ord('a'))%26)

    return result


if __name__ == '__main__':
    print(solution("a B z", 4))