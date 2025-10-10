# 전위,중위순회로 트리 복구하기
X, Y = 'ABDCEGF', 'BDAGECF'

tree = {}
def dfs(x, y):
    if not x:
        return '0'

    center = x[0]
    idx = y.index(center)

    tree[dfs(x[1:idx+1], y[:idx])] = center
    tree[dfs(x[idx+1:], y[idx+1:])] = center
    return center

tree[dfs(X, Y)] = '-1'
print(tree)
# 리프노드(0) 처리 필요

