# O(N): 모든 스택이 내림차순이라면
import sys
input = sys.stdin.readline

def valid(stack):
    for i in range(len(stack)-1):
        if stack[i] < stack[i+1]:
            return False
    return True

N, M = map(int, input().split())
for _ in range(M):
    input()
    stack = list(map(int, input().split()))
    if not valid(stack):
        print('No')
        exit(0)

print('Yes')