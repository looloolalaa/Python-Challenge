"""
최소 바위 거리가 K라면
K보다 큰 거리를 갖는 바위들을 순차적으로 제거
-> 제거 해야 하는 바위 개수를 n과 비교하며 범위 좁히기
"""


def solution(distance, rocks, n):
    rocks.sort()

    def must_remove(min_dis):
        remove = 0
        pos = 0
        for rock in rocks:
            dis = rock - pos
            if dis < min_dis:
                remove += 1
            else:
                pos = rock
        return remove

    start, end = 1, distance
    while start <= end:
        mid = (start + end) // 2
        if must_remove(mid) <= n:
            start = mid + 1
        else:
            end = mid - 1

    return end


if __name__ == '__main__':
    print(solution(25, [2, 14, 11, 21, 17], 2))