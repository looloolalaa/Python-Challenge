# set.remove(4) 런타임 에러 swift 와 다름
# 결과값 res 에 저장하면 메모리 초과 => 즉각 print
import sys
input = sys.stdin.readline

s = set()
M = int(input())
for _ in range(M):
    line = input().split()
    x = -1
    if len(line) == 2:
        x = int(line[1])

    if line[0] == 'add':
        s.add(x)
    elif line[0] == 'remove':
        if x in s:
            s.remove(x)
    elif line[0] == 'check':
        print(1 if x in s else 0)
    elif line[0] == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif line[0] == 'all':
        s = set(i for i in range(1, 21))
    elif line[0] == 'empty':
        s = set()


