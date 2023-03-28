# for else
def solution(park, routes):
    n, m = len(park), len(park[0])

    def valid(p):
        return 0 <= p[0] < n and 0 <= p[1] < m

    s = -1, -1
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                s = i, j
                break

    arrows = {'E': [0, 1], 'W': [0, -1], 'S': [1, 0], 'N': [-1, 0]}
    for r in routes:
        arrow, dist = r.split()
        a = arrows[arrow]
        p = s
        for _ in range(int(dist)):
            p = p[0] + a[0], p[1] + a[1]
            if not valid(p) or park[p[0]][p[1]] == 'X':
                break
        else:
            s = p

    return s