from collections import deque

def distance(maze, start, end):
    # maze = [[1,1,0], [0,1,1]]
    height, width = len(maze), len(maze[0])
    # 방문 가능 여부
    can_go = [row[:] for row in maze]
    # 거리
    dis = [[0 for _ in range(width)] for _ in range(height)]


    def isValid(p):
        return 0<=p[0]<height and 0<=p[1]<width


    near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    que = deque()

    # 시작 값 넣고 방문체크 후 거리 1로 시작
    que.append(start)
    can_go[start[0]][start[1]] = 0
    dis[start[0]][start[1]] = 1

    while que:
        now = que.popleft()
        for n in near:
            next_p = (now[0]+n[0], now[1]+n[1])
            if isValid(next_p) and can_go[next_p[0]][next_p[1]] == 1:
                can_go[next_p[0]][next_p[1]] = 0
                dis[next_p[0]][next_p[1]] = dis[now[0]][now[1]] + 1
                que.append(next_p)

    # for d in dis:
    #     print(d)

    if dis[end[0]][end[1]] == 0:
        return -1
    return dis[end[0]][end[1]]


if __name__ == '__main__':

    # temp = ['..X', 'X..']
    # res = []
    # for t in temp:
    #     t = t.replace('.', '1')
    #     t = t.replace('X', '0')
    #     res.append(list(map(int, list(t))))
    # print(res)

    # sample
    # 4 6
    # 101111
    # 101010
    # 101011
    # 111011
    N, M = map(int, input().split())
    s, e = (0, 0), (N-1, M-1)
    board = [list(map(int, list(input()))) for _ in range(N)]

    print(distance(board, s, e))
