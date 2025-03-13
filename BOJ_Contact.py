# 정규식 패턴 매칭
import re

def valid(s):
    pattern = r'((100+1+)|(01))+'
    return bool(re.fullmatch(pattern, s))

for _ in range(int(input())):
    s = input()
    print('YES' if valid(s) else 'NO')