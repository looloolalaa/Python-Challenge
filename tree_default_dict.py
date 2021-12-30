from collections import defaultdict

if __name__ == '__main__':
    tree = defaultdict(list)
    parents = [-1, 0, 0, 1, 1]

    for node, parent in enumerate(parents):
        tree[parent].append(node)

    # 접근만 하면 바로 생성되므로 주의
    if tree[5]:
        print('list')
    else:
        print('empty')

    print(tree)
