if __name__ == '__main__':
    data = [21, 28, 14, 32, 25, 18, 11, 30, 19, 15]

    tree = {}  # {21: [14, 28], 28: [25, 32] .. }
    root = data[0]
    tree[root] = [-1, -1]

    def insert(r, n):
        if r > n:
            if tree[r][0] == -1:
                tree[r][0] = n
                tree[n] = [-1, -1]
                return
            else:
                insert(tree[r][0], n)
        else:
            if tree[r][1] == -1:
                tree[r][1] = n
                tree[n] = [-1, -1]
                return
            else:
                insert(tree[r][1], n)

    for d in data[1:]:
        insert(root, d)

    print(tree)

    def inOrder(n):
        if n == -1:
            return
        inOrder(tree[n][0])
        print(n)
        inOrder(tree[n][1])


    inOrder(root)