if __name__ == '__main__':
    N = int(input())
    moves = input().split()

    direction = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

    def isvalid(p):
        return 0 <= p[0] < N and 0 <= p[1] < N

    now = [0, 0]
    for m in moves:
        next_n = now[:]
        dx, dy = direction[m][0], direction[m][1]
        next_n = [next_n[0]+dx, next_n[1]+dy]

        if isvalid(next_n):
            now = next_n

    now = [now[0]+1, now[1]+1]
    print(now)