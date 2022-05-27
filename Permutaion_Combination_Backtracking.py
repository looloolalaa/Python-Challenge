"""
dfs - backtracking
"""
if __name__ == '__main__':
    N = 4
    M = 3  # N개중 M개 뽑기
    temp = [10, 20, 30, 40]  # 입력 배열
    result = [0] * M  # 출력 배열
    check = [False] * N  # 방문 확인 배열

    def permutation_dfs(level):
        if level == M:
            print(result)
            return

        for i in range(N):
            if not check[i]:
                check[i] = True
                result[level] = temp[i]
                permutation_dfs(level + 1)
                check[i] = False

    def combination_dfs(level, idx):
        if level == M:
            print(result)
            return
        for i in range(idx, N):
            result[level] = temp[i]
            combination_dfs(level+1, i+1)

    permutation_dfs(0)
    print()
    combination_dfs(0, 0)