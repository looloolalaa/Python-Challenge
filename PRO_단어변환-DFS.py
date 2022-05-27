def solution(begin, target, words):
    answer = []
    visited = [False for _ in range(len(words))]
    if target not in words:
        return 0

    def can_change(word1, word2):
        diff = 0
        for a, b in zip(word1, word2):
            if a != b:
                diff += 1
        return diff <= 1

    def dfs(word, depth):
        if word == target:
            answer.append(depth)
            return
        for i in range(len(words)):
            if not visited[i] and can_change(word, words[i]):
                visited[i] = True
                dfs(words[i], depth + 1)
                visited[i] = False

    dfs(begin, 0)
    # print(answer)
    return min(answer)


if __name__ == '__main__':
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))