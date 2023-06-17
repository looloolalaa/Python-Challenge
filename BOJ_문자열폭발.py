# [:-n] 시간 초과 => n번 pop
s = input()
bomb = input()
n = len(bomb)

stack = []
for c in s:
    stack.append(c)
    if ''.join(stack[-n:]) == bomb:
        # stack = stack[:-n] <- 시간초과
        for _ in range(n):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')