# 무궁화꽃이피었습니다
a, b, d = map(int, input().split())
total = 0

x = d // a
total += x*(a+b)

remain = d % a
total += remain
if remain == 0:
    total -= b

y = d // b
total += y*(a+b)

remain = d % b
total += remain
if remain == 0:
    total -= a

print(total)