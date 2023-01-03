# string handling
def solution(polynomial):
    x, c = 0, 0
    for p in polynomial.split(' + '):
        if p[-1] == 'x':
            if p[:-1]:
                x += int(p[:-1])
            else:
                x += 1
        else:
            c += int(p)

    if x != 0 and c != 0:
        return (str(x) if x != 1 else '') + 'x + ' + str(c)
    return (str(x) if x != 1 else '') + 'x' if x != 0 else str(c)


if __name__ == '__main__':
    print(solution("3x + 7 + x"))