if __name__ == '__main__':
    tree = {}
    root = 0

    def leaf_count(node):
        if node not in tree:
            return 1
        else:
            return sum([leaf_count(child) for child in tree[node]])

    N = int(input())
    parents = list(map(int, input().split()))
    X = int(input())

    if parents[X] == -1:
        print(0)
    else:
        parents[X] = -2
        for i, parent in enumerate(parents):
            if parent == -1:
                root = i
            else:
                if parent not in tree:
                    tree[parent] = [i]
                else:
                    tree[parent].append(i)

        print(leaf_count(root))

