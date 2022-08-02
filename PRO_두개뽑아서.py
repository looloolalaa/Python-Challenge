from itertools import combinations


def solution(numbers):
    return sorted(list(set(map(sum, list(combinations(numbers, 2))))))


if __name__ == '__main__':
    print(solution([2,1,3,4,1]))