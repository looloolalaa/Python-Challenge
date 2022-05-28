N = int(input())
S, G, P, D = map(int, input().split())
grades = input()

month = [0 for _ in range(len(grades)+1)]
max_money = {'B': S-1, 'S': G-1, 'G': P-1, 'P': D-1}

for i, grade in enumerate(grades, 1):
    if grade == 'D':
        month[i] = D
    else:
        month[i] = max_money[grade] - month[i-1]

print(sum(month))