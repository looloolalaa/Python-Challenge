# 선택과 반대선택
from itertools import combinations

def score(sel):
    res = 0
    for i in sel:
        for j in sel:
            if i != j:
                res += table[i][j]
    return res

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

ans = int(1e9)
for sel in combinations(range(n), n//2):
    oppo = list(set(i for i in range(n)) - set(sel))
    ans = min(ans, abs(score(sel) - score(oppo)))
print(ans)