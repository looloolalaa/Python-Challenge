# 하루 인출
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

def count(K):
    money = 0
    cnt = 0
    for a in arr:
        if money < a:
            money = K - a
            cnt += 1
        else:
            money -= a
    return cnt

start, end = max(arr), sum(arr)
while start <= end:
    center = (start + end) // 2
    cnt = count(center)
    if cnt <= M:
        end = center-1
    elif cnt > M:
        start = center+1

print(start)
