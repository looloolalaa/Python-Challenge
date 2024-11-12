# bisect(_, _, lo, hi)
from bisect import bisect_left, bisect_right

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
for i in range(N-2):
    target = -arr[i]
    start, end = i+1, N-1
    while start < end:
        s = arr[start] + arr[end]
        if s < target:
            start += 1
        elif s > target:
            end -= 1
        elif s == target:
            if arr[start] == arr[end]:
                cnt = end - start + 1
                ans += cnt*(cnt-1)//2
                break

            start_right = bisect_right(arr, arr[start], start, end+1)
            end_left = bisect_left(arr, arr[end], start, end+1)
            ans += (start_right - start) * (end - end_left + 1)
            start, end = start_right, end_left-1

print(ans)