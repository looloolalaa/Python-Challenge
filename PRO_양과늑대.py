# 트리 탐색 dfs(cnt)
from collections import defaultdict

def solution(info, edges):
    tree = defaultdict(set)
    for a, b in edges:
        tree[a].add(b)

    ans = 0
    cnt = [0, 0]

    def dfs(canGo):
        if cnt[0] <= cnt[1] and cnt[0] != 0:
            return

        nonlocal ans
        ans = max(ans, cnt[0])
        for a in canGo:
            cnt[info[a]] += 1
            dfs((canGo - {a}) | tree[a])
            cnt[info[a]] -= 1

    dfs({0})
    return ans