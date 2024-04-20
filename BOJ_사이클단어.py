# 2배 문자열에 포함되어있고, 길이가 같다면
N = int(input())
se = set()
def exist(st):
    for s in se:
        if len(s) == len(st) and st in 2*s:
            return True
    return False

for _ in range(N):
    st = input()
    if not exist(st):
        se.add(st)

print(len(se))
