# 몫나머지로 O(n!) 줄이기
from math import factorial

def solution(n, k):
    result = []
    arr = [i + 1 for i in range(n)]

    def first(arr, k):
        if not arr:
            return
        m = len(arr)
        term = factorial(m) // m
        a, b = k // term, k % term
        result.append(arr.pop(a))
        first(arr, b)

    first(arr, k - 1)
    return result

