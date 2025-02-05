# 최소 루트 (최소 삼각형 루트 비슷)
N = int(input())
arr = []
move = []
for _ in range(N-1):
    a, b, c, d = map(int, input().split())
    arr.append([a, b])
    move.append([c, d])
arr.append(list(map(int, input().split())))

for i in range(1, N):
    arr[i][0] += min(arr[i-1][0], arr[i-1][1] + move[i-1][1])
    arr[i][1] += min(arr[i-1][1], arr[i-1][0] + move[i-1][0])

print(min(arr[-1]))