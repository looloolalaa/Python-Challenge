import bisect

def fibo():
    memo = {1: 0, 2: 1}

    # Recursion
    def f_bad(n):
        if n==1 or n==2:
            return n-1
        else:
            return f_bad(n-1) + f_bad(n-2)

    # Top-Down
    def f(n):
        if n not in memo:
            memo[n] = f(n-1) + f(n-2)
        return memo[n]

    # Bottom-Up
    for i in range(3, 41):
        memo[i] = memo[i-1] + memo[i-2]

    print(f(35))
    print(memo[35])
    print(f_bad(35))

def cut_stick():
    pi = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    r = {0: 0}
    for i in range(1, len(pi)):
        candi = [r[j] + pi[i - j] for j in range(i)]
        r[i] = max(candi)
    print(r[7])

def longest_common_substring():
    string_A = 'ABCDEF'
    string_B = 'GBCDFE'
    lcs = [[0 for _ in range(len(string_B) + 1)] for _ in range(len(string_A) + 1)]

    max_len = 0
    max_index = -1, -1
    for i, a in enumerate(string_A):
        for j, b in enumerate(string_B):
            if a == b:
                lcs[i+1][j+1] = lcs[i][j] + 1
                if lcs[i+1][j+1] > max_len:
                    max_len = lcs[i+1][j+1]
                    max_index = i+1, j+1

    for l in lcs:
        print(l)
    print(max_len)
    print(string_A[max_index[0]-max_len:max_index[0]])
    print(string_B[max_index[1] - max_len:max_index[1]])

def longest_common_subsequence():
    string_A = 'ABCDEF'
    string_B = 'GBCDFE'
    lcs = [[0 for _ in range(len(string_B)+1)] for _ in range(len(string_A)+1)]
    for i, a in enumerate(string_A):
        for j, b in enumerate(string_B):
            if a == b:
                lcs[i+1][j+1] = lcs[i][j] + 1
            else:
                lcs[i + 1][j + 1] = max(lcs[i+1][j], lcs[i][j+1])

    for l in lcs:
        print(l)

    results = []

    def dfs(start, result):
        if start[0] == 0 or start[1] == 0:
            results.append(result)
        else:
            here = lcs[start[0]][start[1]]
            up = lcs[start[0]-1][start[1]]
            left = lcs[start[0]][start[1]-1]
            if here == up or here == left:
                if here == up:
                    dfs((start[0] - 1, start[1]), result[:])
                if here == left:
                    dfs((start[0], start[1]-1), result[:])
            else:
                result.append(string_A[start[0]-1])
                dfs((start[0]-1, start[1]-1), result)

    dfs((len(lcs)-1, len(lcs[0])-1), [])
    results = set(''.join(reversed(result)) for result in results)
    print(results)

def knapsack():
    N, K = map(int, input().split())
    goods = []
    for _ in range(N):
        goods.append(list(map(int, input().split())))

    v = [[0 for _ in range(K+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        selected = goods[i-1]
        weight, value = selected[0], selected[1]
        for w in range(1, K+1):
            if w < weight:
                v[i][w] = v[i-1][w]
            else:
                v[i][w] = max(v[i-1][w], value+v[i-1][w-weight])

    # for v in v:
    #     print(v)
    print(v[-1][-1])

def ant_warrior():
    N = int(input())
    food = list(map(int, input().split()))
    a = [0 for _ in range(N)]
    a[0] = food[0]
    a[1] = max(food[0], food[1])
    for i in range(2, N):
        a[i] = max(food[i]+a[i-2], a[i-1])
    # print(a)
    print(a[-1])

def make_one():
    x = int(input())
    a = [-1 for _ in range(x+1)]
    a[1] = 0

    # Top-Down
    def f(i):
        if i-int(i)!=0:
            return float('inf')
        else:
            i = int(i)
            if a[i] == -1:
                a[i] = min(f(i/5), f(i/3), f(i/2), f(i-1))+1
            return a[i]

    # Bottom-Up
    for i in range(2, x+1):
        next_i = []
        if i % 5 == 0:
            next_i.append(i // 5)
        if i % 3 == 0:
            next_i.append(i // 3)
        if i % 2 == 0:
            next_i.append(i // 2)
        next_i.append(i-1)
        a[i] = min([a[j] for j in next_i]) + 1

    print(f(x))
    print(a[x])

def bill():
    N, M = map(int, input().split())
    k = []
    for _ in range(N):
        k.append(int(input()))

    inf = float('inf')
    a = [inf for _ in range(M+1)]
    a[0] = 0

    for i in k:
        for m in range(i, M+1):
            if a[m-i] != inf:
                a[m] = min(a[m], a[m-i] + 1)
    print(a)
    if a[M] == inf:
        print(-1)
    else:
        print(a[M])

def gold_mine():
    answer = []
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        gold = []
        row = []
        for val in list(map(int, input().split())):
            row.append(val)
            if len(row) == m:
                gold.append(row[:])
                row.clear()
        # print(gold)

        def isValid(p):
            return 0<=p[0]<n and 0<=p[1]<m

        for j in range(1, m):
            for i in range(n):
                next_list = [gold[p[0]][p[1]] for p in [(i, j-1), (i-1, j-1), (i+1, j-1)] if isValid(p)]
                gold[i][j] = max(next_list) + gold[i][j]

        result = 0
        for i in range(n):
            result = max(result, gold[i][m-1])
        answer.append(result)


    for a in answer:
        print(a)

def lower_bound(l, x):
    start, end = 0, len(l)
    while start < end:
        mid = (start+end)//2
        if x<=l[mid]:
            end = mid
        else:
            start = mid+1
    return end

def upper_bound(l, x):
    left, right = 0, len(l)
    while left < right:
        mid = (right+left)//2
        if l[mid]<=x:
            left = mid + 1
        else:
            right = mid
    return right

def number_card2():
    N = int(input())
    cards = sorted(list(map(int, input().split())))
    M = int(input())
    numbers = list(map(int, input().split()))

    for num in numbers:
        print(upper_bound(cards, num) - lower_bound(cards, num), end=' ')

def longest_increasing_subsequence():
    a = [3, 5, 7, 9, 2, 1, 4, 8]

    a.insert(0, 0)

    # O(N^2)
    d = [0]
    p = [0]
    for i in range(1, len(a)):
        smaller = [j for j in range(i) if a[j]<a[i]]
        smaller_d = [d[j] for j in smaller]
        for j in smaller:
            if d[j]== max(smaller_d):
                p.append(j)
                break
        d.append(max(smaller_d) + 1)

    index = d.index(max(d))
    ans = []
    while index > 0:
        ans.append(a[index])
        index = p[index]
    print(list(reversed(ans)))

    print(p)
    # print(d)
    print('O(N^2):', max(d))
    print()

    # O(NlogN)
    d = [0]
    for i in range(1, len(a)):
        pos = lower_bound(d, a[i])
        if len(d) == pos:
            d.append(a[i])
        else:
            d[pos] = min(d[pos], a[i])
    # print(d)
    print('O(NlogN):', len(d)-1)

def electric_cord():

    lines = [(0, 0)]
    d = [0]

    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        lines.append((a, b))
    lines.sort()
    lines = list(map(lambda x: x[1], lines))

    for i in range(1, len(lines)):
        smaller = [d[j] for j in range(i) if lines[j]<lines[i]]
        d.append(max(smaller)+1)

    print(n - max(d))

def semiconductor():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)

    d = [0]
    for i in range(1, len(a)):
        pos = bisect.bisect_left(d, a[i])
        if pos == len(d):
            d.append(a[i])
        else:
            d[pos] = min(d[pos], a[i])
    print(len(d)-1)

def soldier_arrange():
    def lower_bound_reverse(l, x):
        left, right = 0, len(l)
        while left<right:
            mid = (left+right)//2
            if x>=l[mid]:
                right = mid
            else:
                left = mid+1
        return right

    N = int(input())
    a = list(map(int, input().split()))
    a.insert(0, float('inf'))

    d = [float('inf')]
    for i in range(1, len(a)):
        pos = lower_bound_reverse(d, a[i])
        if pos == len(d):
            d.append(a[i])
        else:
            d[pos] = max(d[pos], a[i])
        # bigger = [d[j] for j in range(i) if a[j]>a[i]]
        # d.append(max(bigger)+1)
    # print(d)
    print(N-(len(d)-1))


if __name__ == '__main__':
    # fibo()
    # cut_stick()
    # longest_common_substring()
    # longest_common_subsequence()
    # knapsack()
    # ant_warrior()
    # make_one()
    # bill()
    # gold_mine()

    # number_card2()
    # longest_increasing_subsequence()
    # electric_cord()
    # semiconductor()
    soldier_arrange()
