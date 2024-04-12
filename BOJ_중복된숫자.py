# split 메모리 초과 + 시간 pypy3
N = int(input())
line = input() + ' '
temp = ''
s = set()
for c in line:
    if c == ' ':
        if int(temp) in s:
            print(temp)
            break
        s.add(int(temp))
        temp = ''
    else:
        temp += c

