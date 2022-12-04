# string implementation
from collections import Counter


def solution(p):
    def isBalanced(s):
        c = Counter(s)
        return c['('] == c[')']

    def isRight(s):
        temp = s
        while '()' in temp:
            temp = temp.replace('()', '')
        return temp == ''

    def change(w):
        if not w:
            return ''

        u, v = '', ''
        for i in range(2, len(w) + 1, 2):
            if isBalanced(w[:i]):
                u = w[:i]
                v = w[i:]
                break

        if isRight(u):
            return u + change(v)

        result = '(' + change(v) + ')'
        temp = ''.join(['(' if c == ')' else ')' for c in u[1:-1]])
        return result + temp

    return change(p)


if __name__ == '__main__':
    print(solution("()))((()"))