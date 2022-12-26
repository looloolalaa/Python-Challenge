# 대치 행렬 후 내적
def solution(arr1, arr2):
    def inner(a, b):
        return sum(i * j for i, j in zip(a, b))

    result = [[-1 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    inversion = list(zip(*arr2))
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            result[i][j] = inner(arr1[i], inversion[j])
    return result

# 1 4
# 3 2
# 4 1
# 3 2 x 2 2

# # 1 2
# # 3 4

# [_ _]
# [_ _]
# [_ _]
