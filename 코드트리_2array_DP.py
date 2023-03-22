# dp
n = int(input())
table = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    table[i][1:] = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    for j in range(1, n+1):
        table[i][j] += max(table[i][j-1], table[i+1][j])

print(table[0][-1])