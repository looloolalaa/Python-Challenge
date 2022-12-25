# 대치 행렬 후 내적
from itertools import product

def solution(arr1, arr2):
    result = []
    line = []
    for a, b in list(product(arr1, list(zip(*arr2)))):
        line.append(sum([i*j for i, j in list(zip(a, b))]))
        if len(line) == len(arr2[0]):
            result.append(line)
            line = []
    return result


# 1 4
# 3 2
# 4 1


# 1 2
# 3 4