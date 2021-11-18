from collections import deque

def BFS_shortest():
    maze = [
        "XXXXX",
        "OXOOO",
        "OXOXO",
        "OXOOO",
        "OOOXO"
    ]
    dist = [[-1 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    way = [(0,1),(1,0),(0,-1),(-1,0)]
    que = deque()

    def isValid(p):
        return 0<=p[0]<len(maze) and 0<=p[1]<len(maze[0]) and maze[p[0]][p[1]] == 'O' and dist[p[0]][p[1]] == -1

    def color():
        while que:
            here = que.popleft()
            for w in way:
                next_pos = (here[0]+w[0], here[1]+w[1])
                if isValid(next_pos):
                    que.append(next_pos)
                    dist[next_pos[0]][next_pos[1]] = dist[here[0]][here[1]]+1


    dist[1][0] = 0
    que.append((1,0))
    color()

    for d in dist:
        print(d)

def solution(places):
    result = []
    near = [(0,1),(1,0),(0,-1),(-1,0)]
    two = [(0,2),(2,0),(0,-2),(-2,0)]

    def isSafeTable(table):
        def isSafe(pos):
            def isP(p):
                return 0 <= p[0] < 5 and 0 <= p[1] < 5 and table[p[0]][p[1]] == 'P'

            def isO(p):
                return 0 <= p[0] < 5 and 0 <= p[1] < 5 and table[p[0]][p[1]] == 'O'

            for n in near:
                next_p = (pos[0] + n[0], pos[1] + n[1])
                if isP(next_p):
                    return False

            for t, n in zip(two, near):
                if isP((pos[0] + t[0], pos[1] + t[1])) and isO((pos[0] + n[0], pos[1] + n[1])):
                    return False

            if isP((pos[0] + 1, pos[1] + 1)):
                if isO((pos[0], pos[1] + 1)) or isO((pos[0] + 1, pos[1])):
                    return False
            if isP((pos[0] + 1, pos[1] - 1)):
                if isO((pos[0] + 1, pos[1])) or isO((pos[0], pos[1] - 1)):
                    return False
            if isP((pos[0] - 1, pos[1] - 1)):
                if isO((pos[0], pos[1] - 1)) or isO((pos[0] - 1, pos[1])):
                    return False
            if isP((pos[0] - 1, pos[1] + 1)):
                if isO((pos[0], pos[1] + 1)) or isO((pos[0] - 1, pos[1])):
                    return False

            return True

        def isValid(p):
            return 0 <= p[0] < 5 and 0 <= p[1] < 5 and table[p[0]][p[1]] != 'X'

        def existP_nearby(p):
            dist = {p: 0}
            que = deque()
            que.append(p)
            while que:
                here = que.popleft()
                if 0 < dist[here] <= 2 and table[here[0]][here[1]] == 'P':
                    return True
                else:
                    for n in near:
                        next_pos = (here[0] + n[0], here[1] + n[1])
                        if isValid(next_pos) and next_pos not in dist and dist[here] < 2:
                            dist[next_pos] = dist[here] + 1
                            que.append(next_pos)

            return False


        for i in range(5):
            for j in range(5):
                # if table[i][j] == 'P' and not isSafe((i, j)):
                if table[i][j] == 'P' and existP_nearby((i, j)):
                    return 0
        return 1


    for place in places:
        table = [row for row in place]
        result.append(isSafeTable(table))

    return result


if __name__ == '__main__':
    example = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(example))