# 듬성듬성 dfs
N = int(input())
line = list(input())

def inserted(t):
    li = line[:]
    for i in reversed(t):
        li.insert(i+2, ')')
        li.insert(i-1, '(')
    return ''.join(li)

ans = -float('inf')
temp = []
def dfs(s):
    global ans
    ans = max(ans, eval(inserted(temp)))

    for j in range(s, N, 2):
        temp.append(j)
        dfs(j+4)
        temp.pop()

dfs(1)
print(ans)
