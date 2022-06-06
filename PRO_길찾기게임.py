"""
Binary Tree
"""
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)  # python recursion limit


def solution(nodeinfo):
    n_x = {}  # {7: 8, 4: 3, ..}
    height = defaultdict(list)  # {5: [(4, [3, 5]), (2, [11, 5])], 6: [(7, [8, 6])]}
    for t in enumerate(nodeinfo, 1):
        height[t[1][1]].append(t)  # {y: [(n, [x, y])]}
        n_x[t[0]] = t[1][0]  # {node: x}

    root = height[max(height.keys())][0][0]

    tree = {root: [-1, -1]}
    for h in sorted(height.keys(), reverse=True)[1:]:  # from the top
        for n, (x, y) in height[h]:
            i = root
            while True:
                lor = 0 if x < n_x[i] else 1  # left or right
                if tree[i][lor] == -1:  # right child 를 봤는데 비어 있다면
                    tree[i][lor] = n  # 그곳에 노드를 넣고
                    tree[n] = [-1, -1]  # 비어 있는 child 추가
                    break
                i = tree[i][lor]  # 비어 있지 않다면 내려간다.

    pre, post = [], []

    def dfs(n):  # Pre, Post at the same time
        if n == -1:
            return
        pre.append(n)
        dfs(tree[n][0])
        dfs(tree[n][1])
        post.append(n)

    dfs(root)
    return [pre, post]



if __name__ == '__main__':
    print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))