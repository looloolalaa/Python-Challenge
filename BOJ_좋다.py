# 배열에서 위치가 다른 두 숫자의 합으로
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
for i in range(N):
    start, end = 0, N-1
    while start < end:
        if start == i:
            start += 1
        if end == i:
            end -= 1
        if start >= end:
            break

        if arr[i] < arr[start] + arr[end]:
            end -= 1
        elif arr[i] > arr[start] + arr[end]:
            start += 1
        else:
            ans += 1
            break

print(ans)