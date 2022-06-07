import sys
sys.setrecursionlimit(10**6)  # python recursion limit


def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    root = max(nodeinfo, key=lambda x: x[1])

    tree = {}
    def set_tree(nodes):
        if not nodes:
            return None
        root = max(nodes, key=lambda x: x[1])
        left = list(filter(lambda x: x[0] < root[0], nodes))
        right = list(filter(lambda x: x[0] > root[0], nodes))
        tree[root[2]] = [set_tree(left), set_tree(right)]
        return root[2]

    pre, post = [], []
    def dfs(n):
        if not n:
            return
        pre.append(n)
        dfs(tree[n][0])
        dfs(tree[n][1])
        post.append(n)

    set_tree(nodeinfo)
    dfs(root[2])

    return [pre, post]


if __name__ == '__main__':
    print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))