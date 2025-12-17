# 접두사 관계 고민
from bisect import bisect_left
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = [input() for _ in range(N)]
words.sort()

ans = 0
for _ in range(M):
    word = input().strip()

    i = bisect_left(words, word)
    if i < len(words) and words[i].startswith(word):
        ans += 1

print(ans)
