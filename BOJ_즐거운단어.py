# 경우의 수(가짓수) dfs(1*cnt)
s = input()

ans = 0
def dfs(i, cnt, mo, ja, L):
    if mo >= 3 or ja >= 3:
        return

    if i == len(s):
        if L:
            global ans
            ans += cnt
        return

    if s[i] == '_':
        dfs(i+1, cnt*5, mo+1, 0, L)
        dfs(i+1, cnt, 0, ja+1, True)
        dfs(i+1, cnt*20, 0, ja+1, L)

    else:
        if s[i] in 'AEIOU':
            mo, ja = mo+1, 0
        else:
            mo, ja = 0, ja+1

        if s[i] == 'L':
            L = True

        dfs(i+1, cnt, mo, ja, L)

dfs(0, 1, 0, 0, False)
print(ans)