def fibo():
    memo = {0: 0, 1: 1}

    def f(n):
        if n not in memo:
            memo[n] = f(n-1) + f(n-2)
        return memo[n]
    print(f(40))

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


if __name__ == '__main__':
    # fibo()
    # cut_stick()
    # longest_common_substring()
    # longest_common_subsequence()
    # knapsack()
    ant_warrior()