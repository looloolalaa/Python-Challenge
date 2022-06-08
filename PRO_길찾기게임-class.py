import sys
sys.setrecursionlimit(10**6)  # python recursion limit


class Tree:
    def __init__(self, nodes):
        if not nodes:
            self.root = None
        else:
            self.root = max(nodes, key=lambda x: x[1])
            self.num = self.root[2]
            self.left = Tree(list(filter(lambda x: x[0] < self.root[0], nodes)))
            self.right = Tree(list(filter(lambda x: x[0] > self.root[0], nodes)))


def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)

    pre, post = [], []

    def dfs(t):
        if not t.root:
            return
        pre.append(t.num)
        dfs(t.left)
        dfs(t.right)
        post.append(t.num)

    tree = Tree(nodeinfo)
    dfs(tree)

    return [pre, post]


if __name__ == '__main__':
    print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))