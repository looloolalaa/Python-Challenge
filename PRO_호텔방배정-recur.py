"""
경로 압축 - recursion
"""
import sys
sys.setrecursionlimit(10**6)


def solution(k, room_number):
    room = {}

    def point(i):  # next position
        if i not in room:
            room[i] = i + 1
            return i
        room[i] = point(room[i])
        return room[i]

    return [point(n) for n in room_number]


if __name__ == '__main__':
    print(solution(10, [1,3,4,1,3,1]))