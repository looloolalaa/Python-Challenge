# 배수 개수
n = int(input())
arr = list(map(int, input().split()))

def cnt(x):
    res = 0
    for a in arr:
        if a % x == 0:
            res += 1
    return res


print(max(cnt(i) for i in range(2, 101)))


