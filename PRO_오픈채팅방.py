# string handling
def solution(record):
    book = {}

    result = []
    for r in record:
        if r.startswith('Leave'):
            _, uid = r.split()
            result.append((uid, False))
        else:
            order, uid, name = r.split()
            book[uid] = name
            if order == 'Enter':
                result.append((uid, True))

    return [book[uid] + ('님이 들어왔습니다.' if enter else '님이 나갔습니다.') for uid, enter in result]


if __name__ == '__main__':
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))