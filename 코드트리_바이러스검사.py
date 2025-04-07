# 몫 나머지(+1)
n = int(input())
arr = list(map(int, input().split()))
x, y = map(int, input().split())
ans = n
for i in range(n):
    arr[i] = 0 if arr[i] - x < 0 else arr[i] - x

for a in arr:
    ans += a//y
    if a % y > 0:
        ans += 1
print(ans)