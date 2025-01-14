# 끝나는 시간 정렬
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: x[1])

end = 0
cnt = 0
for s, e in arr:
    if s < end:
        continue

    cnt += 1
    end = e

print(cnt)