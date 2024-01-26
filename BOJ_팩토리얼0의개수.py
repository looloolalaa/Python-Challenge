from math import factorial

N = int(input())

result = 0
num = factorial(N)
while num % 10 == 0:
    result += 1
    num //= 10

print(result)