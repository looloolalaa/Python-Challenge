# string queue
from collections import deque


def solution(msg):
    book = {'': 0}
    i = 1
    while i <= 26:
        book[chr(ord('A') + i - 1)] = i
        i += 1

    result = []
    msg = deque(msg)

    while msg:
        w = ''
        while msg and w in book:
            w += msg.popleft()

        if not msg:
            if w in book:
                result.append(book[w])
                break

        c = w[-1]
        w = w[:-1]
        result.append(book[w])
        book[w + c] = i
        i += 1
        msg.appendleft(c)

    return result


if __name__ == '__main__':
    print(solution('KAKAO'))