# arr[i][j] == set()
def solution(grid):
    height, width = len(grid), len(grid[0])
    visited = [[set() for _ in range(width)] for _ in range(height)]

    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    result = []

    def plus(p, d):
        return (p[0] + dxy[d][0] + height) % height, (p[1] + dxy[d][1] + width) % width

    def go(start):
        for d in range(4):
            path, p = 0, start
            while True:
                if d in visited[p[0]][p[1]]:
                    break
                visited[p[0]][p[1]].add(d)
                path += 1

                p = plus(p, d)
                ch = grid[p[0]][p[1]]

                if ch == "R":
                    d = (d + 1) % 4
                elif ch == "L":
                    d = (d - 1 + 4) % 4

                if p == start and d in visited[p[0]][p[1]]:
                    result.append(path)
                    break

    for i in range(height):
        for j in range(width):
            go((i, j))

    return sorted(result)