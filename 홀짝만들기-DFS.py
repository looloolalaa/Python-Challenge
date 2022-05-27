a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

temp = [a, b, c]
answer = []


# n: 바로 전 출력 된 숫자, box: 업데이트 해가는 정답
def dfs(n, box):
    if len(box) == len(temp):
        answer.append(box)
        return
    for j in temp[len(box)]:
        if (n % 2 and not j % 2) or (not n % 2 and j % 2):
            new_box = box[:]
            new_box.append(j)
            dfs(j, new_box)


# 짝수로 시작했을 때
dfs(0, [])
# 홀수로 시작했을 때
dfs(1, [])
print(answer)
