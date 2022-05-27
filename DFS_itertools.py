if __name__ == '__main__':
    n, m = 4, 2
    cards = [4,5,6,7]

    visited = [False for _ in range(len(cards))]
    result = [0]*m

    def dfs_Per(i):
        if i == len(result):
            print(result)
            return
        for j in range(len(visited)):
            if not visited[j]:
                result[i] = cards[j]
                visited[j] = True
                dfs_Per(i+1)
                visited[j] = False

    def dfs_Com(i, start):
        if i == len(result):
            print(result)
            return
        for j in range(start, len(cards)):
            result[i] = cards[j]
            dfs_Com(i+1, j+1)

    def dfs_Com_Rep(i, start):
        if i == len(result):
            print(result)
            return
        for j in range(start, len(cards)):
            result[i] = cards[j]
            dfs_Com_Rep(i+1, j)

    def dfs_Pro(i):
        if i == len(result):
            print(result)
            return
        for c in cards:
            result[i] = c
            dfs_Pro(i+1)

    # dfs_Per(0)
    # dfs_Com(0, 0)
    # dfs_Com_Rep(0, 0)
    dfs_Pro(0)