if __name__ == '__main__':
    temp = [[1, 2],
            [3, 4],
            [5, 6]]
    """
    one line rotate
    """
    def rotate90(arr):
        return list(zip(*arr[::-1]))

    def rotate180(arr):
        return list(map(list, map(reversed, arr[::-1])))

    def rotate270(arr):
        return list(reversed(list(zip(*arr))))

    """
    new matrix rotate
    """
    def rotate_90(arr):
        n, m = len(arr), len(arr[0])
        new_arr = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new_arr[j][n-i-1] = arr[i][j]
        return new_arr

    def rotate_180(arr):
        n, m = len(arr), len(arr[0])
        new_arr = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                new_arr[n-i-1][m-j-1] = arr[i][j]
        return new_arr

    def rotate_270(arr):
        n, m = len(arr), len(arr[0])
        new_arr = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new_arr[m - j - 1][i] = arr[i][j]
        return new_arr

    for t in rotate180(temp):
        print(t)

