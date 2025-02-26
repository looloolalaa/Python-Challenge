# 분할정복 + dp
N = int(input())
string = input()

dp = {}
def get_dp(s, e):
    if (s, e) in dp:
        return dp[(s, e)]

    if s == e:
        dp[(s, e)] = [int(string[s]), int(string[s])]
        return dp[(s, e)]

    mini, maxi = float('inf'), -float('inf')
    for k in range(s+1, e, 2):
        front = get_dp(s, k-1)
        rear = get_dp(k+1, e)
        mi, ma = -1, -1
        if string[k] == '+':
            mi = front[0] + rear[0]
            ma = front[1] + rear[1]
        elif string[k] == '-':
            mi = front[0] - rear[1]
            ma = front[1] - rear[0]
        elif string[k] == '*':
            comb = [front[0]*rear[0], front[0]*rear[1], front[1]*rear[0], front[1]*rear[1]]
            mi = min(comb)
            ma = max(comb)

        mini = min(mini, mi)
        maxi = max(maxi, ma)

    dp[(s, e)] = [mini, maxi]
    return dp[(s, e)]

print(get_dp(0, N-1)[1])
