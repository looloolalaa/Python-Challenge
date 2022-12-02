# 3 directions
def solution(n):
    dxy = [(1, 0), (0, 1), (-1, -1)]
    table = [[0 for _ in range(i + 1)] for i in range(n)]

    now, d = (0, 0), 0
    for num in range(1, n * (n + 1) // 2 + 1):
        table[now[0]][now[1]] = num
        follow = (now[0] + dxy[d][0], now[1] + dxy[d][1])
        if not (0 <= follow[0] < n and 0 <= follow[1] < len(table[follow[0]])) or table[follow[0]][follow[1]] != 0:
            d = (d + 1) % 3
            follow = (now[0] + dxy[d][0], now[1] + dxy[d][1])
        now = follow

    result = []
    for line in table:
        result.extend(line)
    return result


if __name__ == '__main__':
    print(solution(6))