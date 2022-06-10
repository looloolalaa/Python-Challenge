if __name__ == '__main__':
    tree = {}
    N = int(input())
    for _ in range(N):
        parent, left, right = input().split()
        tree[parent] = [left, right]

    order = [[], [], []]

    def dfs(n):
        if n == '.':
            return
        order[0].append(n)
        dfs(tree[n][0])
        order[1].append(n)
        dfs(tree[n][1])
        order[2].append(n)


    dfs('A')
    for o in order:
        print(''.join(o))