# 어려운 스택 문제
from collections import deque

n = int(input())
nums = deque([i for i in range(1, n+1)])
stack = []
wanted = deque()
for _ in range(n):
    wanted.append(int(input()))


answer = []
while wanted:
    w = wanted.popleft()
    if stack and stack[-1] == w:
        answer.append('-')
        stack.pop()
    else:
        if not nums:
            print('NO')
            exit(0)
        while nums and nums[0] != w:
            stack.append(nums.popleft())
            answer.append('+')
        if not nums:
            print('NO')
            exit(0)
        nums.popleft()
        answer.append('+')
        answer.append('-')

for a in answer:
    print(a)


