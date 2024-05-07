# 괄호 위치 dfs
_ = int(input())
string = input()

def calc(order):
    s = list(string)
    for i in reversed(order):
        s[i:i+3] = [str(eval(''.join(s[i:i+3])))]

    while len(s) > 1:
        s[:3] = [str(eval(''.join(s[:3])))]
    return s

ans = -float('inf')
temp = []
def dfs(i):
    global ans
    ans = max(ans, int(calc(temp)[0]))
    if i > len(string)-2:
        return

    for j in range(i, len(string)-2, 2):
        temp.append(j)
        dfs(j+4)
        temp.pop()

dfs(0)
print(ans)