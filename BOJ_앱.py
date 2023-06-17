# 크기에 따른 딕셔너리 변화
N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

maxi = {0: 0}
for co, me in zip(cost, memory):
    new_maxi = {}
    for c, m in maxi.items():
        new_cost = co + c
        if new_cost not in maxi:
            new_maxi[new_cost] = me + m
        else:
            new_maxi[new_cost] = max(maxi[new_cost], me + m)

    for k in new_maxi:
        maxi[k] = new_maxi[k]


result = float('inf')
for c in maxi:
    if maxi[c] >= M:
        result = min(result, c)

print(result)
