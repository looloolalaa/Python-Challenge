# 시간초과: 0에서 더하면서 모든 경우 탐색
# 정답: 시작에서 빼면서 다 0으로 만들 수 있는가
scores = [list(map(int, input().split())) for _ in range(4)]

temp = [0 for _ in range(18)]
ab = [(i, j) for i in range(6) for j in range(i+1, 6)]

found = False

def dfs(i):
    global found
    if found:
        return

    if i == 15:
        if all(t == 0 for t in temp):
            found = True
        return

    a, b = ab[i]
    a, b = 3*a, 3*b

    if temp[a] > 0 and temp[b+2] > 0:
        temp[a] -= 1
        temp[b+2] -= 1
        dfs(i+1)
        temp[a] += 1
        temp[b+2] += 1

    if temp[a+1] > 0 and temp[b+1] > 0:
        temp[a+1] -= 1
        temp[b+1] -= 1
        dfs(i+1)
        temp[a+1] += 1
        temp[b+1] += 1

    if temp[a+2] > 0 and temp[b] > 0:
        temp[a+2] -= 1
        temp[b] -= 1
        dfs(i+1)
        temp[a+2] += 1
        temp[b] += 1


result = []
for score in scores:
    temp = score[:]
    found = False
    dfs(0)
    result.append(1 if found else 0)

print(*result)
