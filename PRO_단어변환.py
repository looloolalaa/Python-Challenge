"""
set DFS
"""


def solution(begin, target, words):
    answer = []
    words = set(words)
    if target not in words:
        return 0

    def get_can_go(t, ws):
        def can_change(a):
            diff = 0
            for i, j in zip(t, a):
                if i != j:
                    diff += 1
            return diff <= 1

        return set(filter(can_change, ws))

    def dfs(t, ws, depth):
        # print(t, ws, depth)
        can_go = get_can_go(t, ws)
        if target in can_go:
            answer.append(depth + 1)
            return

        if can_go:
            for go in can_go:
                new_set = ws.copy()
                new_set.remove(go)
                dfs(go, new_set, depth + 1)

    dfs(begin, words, 0)
    return min(answer)


if __name__ == '__main__':
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))