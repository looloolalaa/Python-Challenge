# 회전하면서
# (번호->좌표) (좌표->번호) 입력
if __name__ == '__main__':
    n = 5
    table = [[0 for _ in range(n)] for _ in range(n)]
    center = (n//2, n//2)

    num_to_p = {0: center}  # 0: (2, 2)
    p_to_num = {center: 0}  # (2, 2): 0

    # 회전 순서
    dxy = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # i == 번호, j == 방향(d)
    i, j = 1, 0
    # level == 반복 횟수 (1, 1, 2, 2, 3, 3, 4, 4 ..)
    level = 1

    now = center
    while i < n*n:
        d = dxy[j]
        # d 방향으로 level 만큼 입력
        for _ in range(level):
            now = now[0] + d[0], now[1] + d[1]
            num_to_p[i] = now
            p_to_num[now] = i
            i += 1
            if i >= n*n:
                break

        # 다음 방향으로
        j = (j + 1) % 4
        if j % 2 == 0:
            level += 1


    print(num_to_p)
    print(p_to_num)
