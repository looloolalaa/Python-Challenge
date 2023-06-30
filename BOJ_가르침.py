# 함부로 continue 로 범위 제한 하지 말 것
from itertools import combinations

N, K = map(int, input().split())

words = [set(input()) for _ in range(N)]

if K < 5:
    print(0)
    exit()

K -= 5

candis = []
for word in words:
    need = word - set('antic')
    # if len(need) > K:
    #     continue
    candis.append(need)


alphas = set()
for c in candis:
    alphas |= c

result = 0
if len(alphas) <= K:
    print(N)
    exit()

for teach in combinations(alphas, K):
    teach = set(teach)

    count = 0
    for c in candis:
        if teach >= c:
            count += 1

    result = max(result, count)

print(result)