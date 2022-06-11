def solution(sales, links):
    tree = {}
    d = {}

    def init_tree():
        for link in links:
            parent = link[0]
            child = link[1]
            if parent in tree:
                tree[parent].append(child)
            else:
                tree[parent] = [child]

    def sum_child(root):
        return sum([min(d[child][0], d[child][1]) for child in tree[root]])

    def get_d(root):
        if root in tree:
            children = tree[root]
            for child in children:
                if d[child][1] < d[child][0]:
                    d[root] = [sum_child(root)]
                    break
            else:
                diff = [d[child][1] - d[child][0] for child in children]
                d[root] = [sum_child(root) + min(diff)]
            d[root].append(sales[root-1] + sum_child(root))
        else:
            d[root] = [0]
            d[root].append(sales[root-1])


    def dfs(root):
        if root in tree:
            for child in tree[root]:
                dfs(child)
        get_d(root)

    init_tree()
    dfs(1)

    return min(d[1])


if __name__ == '__main__':
    print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))