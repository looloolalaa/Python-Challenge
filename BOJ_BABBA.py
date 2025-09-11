# A,B 변하기
K = int(input())

A, B = 1, 0
for _ in range(K):
    A, B = B, B + A

print(A, B)
