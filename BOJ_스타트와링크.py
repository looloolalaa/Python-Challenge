# 두 팀 가르기
from itertools import combinations

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

result = float('inf')
people = set(i for i in range(N))
for team in combinations(people, N//2):
    team = set(team)
    a = 0
    for i, j in combinations(team, 2):
        a += table[i][j]
        a += table[j][i]
    b = 0
    for i, j in combinations(people-team, 2):
        b += table[i][j]
        b += table[j][i]

    result = min(result, abs(a - b))

print(result)