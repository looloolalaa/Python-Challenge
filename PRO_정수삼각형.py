"""
한 라인씩 더해가기
"""


def solution(triangle):
    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i - 1][0]
        triangle[i][-1] += triangle[i - 1][-1]
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])

    # print(triangle)
    return max(triangle[-1])


if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))