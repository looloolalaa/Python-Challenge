# upper & lower
def solution(s):
    def change(word):
        return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word))
    return ' '.join(map(change, s.split(' ')))


if __name__ == '__main__':
    print(solution("try hello world"))