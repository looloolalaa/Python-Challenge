# k개 뽑아서 줄 세우기 == nPk
from itertools import permutations

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]

print(len(set(''.join(p) for p in permutations(cards, k))))