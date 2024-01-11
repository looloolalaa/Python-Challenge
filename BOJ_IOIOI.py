# 연속 개수 세기
N = int(input())
M = int(input())
S = input()

result = 0
i, count = 0, 0
while i <= M - 3:
    if S[i:i+3] == 'IOI':
        count += 1
        i += 2
        if count == N:
            result += 1
            count -= 1
    else:
        count = 0
        i += 1

print(result)