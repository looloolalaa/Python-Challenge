# 곱 or 합
from collections import Counter
n, k = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0
counter = Counter()
for card in cards:
    div = k / card
    ans += counter[div]
    counter[card] += 1

print(ans)