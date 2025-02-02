# 무게당 가장 비싼 것 털기
W, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: -x[1])

total = 0
for m, p in arr:
    if W <= 0:
        break

    mini = min(W, m)
    total += mini * p
    W -= mini

print(total)