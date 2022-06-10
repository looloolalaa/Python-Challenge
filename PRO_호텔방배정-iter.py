"""
경로 압축 - iteration
"""


def solution(k, room_number):
    room = {}
    answer = []
    for n in room_number:
        i = n
        visit = [i]
        while i in room:
            i = room[i]
            visit.append(i)
        answer.append(i)
        for v in visit:
            room[v] = i+1
    return answer


if __name__ == '__main__':
    print(solution(10, [1,3,4,1,3,1]))