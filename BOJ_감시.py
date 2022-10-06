# four directions - all search
# dfs(i, watched | new_watched)

# backtracking(dfs)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

cctvs = []
zero_count = 0
for i in range(n):
    for j in range(m):
        if 1 <= table[i][j] <= 5:
            cctvs.append((i, j))
        if table[i][j] == 0:
            zero_count += 1


cases = {1: [(1,), (2,), (3,), (4,)],
         2: [(1,3), (2,4)],
         3: [(1,2), (2,3), (3,4), (4,1)],
         4: [(1,2,3), (1,2,4), (1,3,4), (2,3,4)],
         5: [(1,2,3,4)]}
arrows = {1: (0, 1), 2: (1, 0), 3: (0, -1), 4: (-1, 0)}
candis = []
max_watch_count = -float('inf')



def can_watch(p):
    p_sets = []
    for case in cases[table[p[0]][p[1]]]:
        p_set = set()
        for c in case:
            arrow = arrows[c]
            x = (p[0] + arrow[0], p[1] + arrow[1])
            while 0 <= x[0] < n and 0 <= x[1] < m and table[x[0]][x[1]] != 6:
                if table[x[0]][x[1]] == 0:
                    p_set.add(x)
                x = (x[0] + arrow[0], x[1] + arrow[1])

        p_sets.append(p_set)
    return p_sets


def dfs(i, watched):
    if i == len(cctvs):
        global max_watch_count
        if max_watch_count < len(watched):
            max_watch_count = len(watched)
        return

    p = cctvs[i]
    for p_set in can_watch(p):
        dfs(i + 1, watched | p_set)


dfs(0, set())
print(zero_count - max_watch_count)