# 10! * 55 => 10!
from itertools import permutations

N = int(input())
ans = list(map(int, input().split()))
arr = [i for i in range(1, N+1)]

for line in permutations(arr, N):
    order = []
    for i in range(1, N + 1):
        count = len([left for left in line[:line.index(i)] if left > i])
        if ans[i-1] == count:
            order.append(count)
        else:
            break

    if len(order) == N:
        for l in line:
            print(l, end=' ')

