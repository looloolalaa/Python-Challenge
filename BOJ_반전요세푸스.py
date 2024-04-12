# 음수 인덱스 나머지
N, K, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

way = True
res = []
i = 0
while arr:
    i = i + ((K-1) if way else -K)
    i %= len(arr)
    res.append(arr.pop(i))

    if len(res) % M == 0:
        way = not way

for r in res:
    print(r)

