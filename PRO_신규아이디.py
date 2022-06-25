def solution(new_id):
    answer = ''
    new_id = new_id.lower()

    for c in new_id:
        if c.islower() or c.isdigit() or c in {'-', '_', '.'}:
            answer += c

    while '..' in answer:
        answer = answer.replace('..', '.')

    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]

    if not answer:
        answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
    return answer


if __name__ == '__main__':
    print(solution("...!@BaT#*..y.abcdefghijklm"))
