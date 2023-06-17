# 공동 등수
N, K = map(int, input().split())
scores = []
book = {}
for _ in range(N):
    li = list(map(int, input().split()))
    score = (li[1], li[2], li[3])
    book[li[0]] = score
    scores.append(score)

scores.sort(reverse=True)
print(scores.index(book[K]) + 1)