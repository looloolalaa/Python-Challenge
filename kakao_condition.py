def lower_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:  # left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return right

def solution(info, query):
    answer = []

    comb = [(),
            (0,), (1,), (2,), (3,),
            (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3),
            (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3),
            (0, 1, 2, 3)]

    book = {}

    for person in info:
        person = person.split()
        for c in comb:
            data = person[:-1]
            score = int(person[-1])
            for i in c:
                data[i] = '-'
            key = ' '.join(data)
            if key in book:
                book[key].append(score)
            else:
                book[key] = [score]

    for val in book.values():
        val.sort()

    for q in query:
        # q = q.split()
        # while 'and' in q:
        #     q.remove('and')
        # key = ' '.join(q[:-1])
        # score = int(q[-1])

        q = q.split(' and ')
        key = ' '.join(q[:-1]) + ' ' + q[-1].split()[0]
        score = int(q[-1].split()[1])

        if key not in book:
            answer.append(0)
        else:
            point = lower_bound(book[key], score)
            answer.append(len(book[key]) - point)

    return answer




if __name__=='__main__':
    info = ["java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100",
             "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250",
             "- and backend and senior and - 150",
             "- and - and - and chicken 100",
             "- and - and - and - 150"]

    print(solution(info, query))
