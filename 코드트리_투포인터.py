# 모두 양수일 때 가능
n, a, b = map(int, input().split())
arr = list(map(int, input().split()))

x, y = 0, 0
s = arr[0]

dist = float('inf')
while x < n:
    if a <= s <= b:
        dist = min(dist, y-x+1)
        s -= arr[x]
        x += 1

    elif s < a:
        y += 1
        if y >= n:
            break
        s += arr[y]
    elif s > b:
        s -= arr[x]
        x += 1

print(dist if dist != float('inf') else -1)