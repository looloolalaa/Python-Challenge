def distance(maze, s, e):
    que = []
    que.append(s)
    maze[s[0]][s[1]] = -1

    def isValid(p):
        return 0<=p[0]<len(maze) and 0<=p[1]<len(maze[0]) and maze[p[0]][p[1]] == 1

    while que:
        here = que.pop(0)
        here_dis = maze[here[0]][here[1]]
        next = [(here[0]-1, here[1]),
                (here[0], here[1]+1),
                (here[0]+1, here[1]),
                (here[0], here[1]-1)]
        for n in next:
            if isValid(n):
                que.append(n)
                maze[n[0]][n[1]] = here_dis - 1



if __name__ == '__main__':
    s = (3, 2)
    e = (5, 5)
    maze = [
        [1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 1]
    ]
    maze = [
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1]
    ]
    e = (4, 4)
    distance(maze, s, e)
    for m in maze:
        print(m)
    print(maze[e[0]][e[1]])
