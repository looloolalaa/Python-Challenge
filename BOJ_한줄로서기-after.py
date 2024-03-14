# zeroCnt
N = int(input())
arr = list(map(int, input().split()))

res = [0 for _ in range(N)]
for i in range(N):
    zero = 0
    for j in range(N):
        if zero == arr[i] and res[j] == 0:
            res[j] = i + 1
            break
        if res[j] == 0:
            zero += 1

print(' '.join(map(str, res)))