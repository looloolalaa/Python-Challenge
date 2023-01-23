# go swift code
from math import log2

result = True


def solution(numbers):
    def valid(n):
        global result
        result = True

        b = bin(n)[2:]
        length = 2 ** (int(log2(len(b))) + 1) - 1
        b = b.zfill(length)

        def dfs(s):
            if len(s) == 1:
                return

            quar = (len(s) + 1) // 4
            center = len(s) // 2
            if s[center] == '0' and (s[quar - 1] == '1' or s[quar * 3 - 1] == '1'):
                global result
                result = False
                return
            dfs(s[:center])
            dfs(s[center + 1:])

        dfs(b)
        return result

    return [1 if valid(num) else 0 for num in numbers]


if __name__ == '__main__':
    print(solution([63, 111, 95]))
