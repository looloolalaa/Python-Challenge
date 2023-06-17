# 나를 접두사로 삼는 놈들이 뒤에 아무도 없으면
# 접두사X
N = int(input())
data = [input() for _ in range(N)]
data.sort()


res = 0
for i in range(N):
    if all(not d.startswith(data[i]) for d in data[i+1:]):
        res += 1

print(res)