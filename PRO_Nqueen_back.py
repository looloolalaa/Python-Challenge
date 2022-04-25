"""
1차원 배열 Backtracking
This is quite slow ...
C++ is faster than python although same algorithm
"""


def solution(n):
    table = [-1 for _ in range(n)]
    answer = []

    def isvalid(row):
        for i in range(row):
            if table[row] == table[i] or abs(table[row]-table[i]) == row - i:
                return False
        return True

    def check(row):
        if row == n:
            answer.append(table[:])
            return

        for j in range(n):
            table[row] = j
            if isvalid(row):
                check(row+1)

    check(0)
    # print(answer)

    return len(answer)


if __name__ == '__main__':
    print(solution(5))