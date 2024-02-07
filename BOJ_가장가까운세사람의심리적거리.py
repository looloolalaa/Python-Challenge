from itertools import combinations
from collections import Counter

def score(a, b, c):
    ab = sum(a[i] != b[i] for i in range(4))
    bc = sum(b[i] != c[i] for i in range(4))
    ca = sum(c[i] != a[i] for i in range(4))
    return ab + bc + ca

result = []
T = int(input())
for _ in range(T):
    N = int(input())
    people = input().split()
    counter = Counter(people)

    for v in counter.values():
        if v >= 3:
            result.append(0)
            break
    else:
        result.append(min(score(com[0], com[1], com[2]) for com in combinations(people, 3)))

for r in result:
    print(r)
