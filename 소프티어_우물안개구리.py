# 최고 관계
N, M = map(int, input().split())
arr = list(map(int, input().split()))

best = [True for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1

    if arr[a] < arr[b]:
        best[a] = False
    elif arr[a] > arr[b]:
        best[b] = False
    elif arr[a] == arr[b]:
        best[a] = False
        best[b] = False

print(sum(best))