def solution(arr1, arr2):
    return [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]


if __name__ == '__main__':
    print(solution([[1,2],[2,3]], [[3,4],[5,6]]))