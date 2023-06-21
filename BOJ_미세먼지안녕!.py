# spread & clean
R, C, T = map(int, input().split())

table = []
for _ in range(R):
    table.append(list(map(int, input().split())))


cleaner = [-1, -1]
for i in range(R):
    if table[i][0] == -1:
        cleaner[0] = i
        cleaner[1] = i+1
        break

def valid(i, j):
    return 0 <= i < R and 0 <= j < C
dxy = [[0, 1], [-1, 0], [0, -1], [1, 0]]
upOrder = []
d = 0
start = [cleaner[0], 0 + dxy[d][1]]
while table[start[0]][start[1]] != -1:
    upOrder.append(start)

    if not valid(start[0]+dxy[d][0], start[1]+dxy[d][1]):
        d = (d+1) % 4
    start = [start[0]+dxy[d][0], start[1]+dxy[d][1]]


downOrder = []
d = 0
start = [cleaner[1], 0 + dxy[d][1]]
while table[start[0]][start[1]] != -1:
    downOrder.append(start)

    if not valid(start[0]+dxy[d][0], start[1]+dxy[d][1]):
        d = (d-1 + 4) % 4
    start = [start[0]+dxy[d][0], start[1]+dxy[d][1]]



def spread():
    change = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):

            if table[i][j] > 0:
                spr = []
                for d in dxy:
                    a, b = i+d[0], j+d[1]
                    if not valid(a, b) or table[a][b] == -1:
                        continue
                    spr.append([a, b])

                Arc = table[i][j]
                for a in spr:
                    change[a[0]][a[1]] += Arc//5
                change[i][j] -= (Arc//5)*len(spr)

    for i in range(R):
        for j in range(C):
            table[i][j] += change[i][j]


def clean():
    la = upOrder[-1]
    table[la[0]][la[1]] = 0
    for i in range(len(upOrder)-1, 0, -1):
        a, b = upOrder[i], upOrder[i-1]
        table[a[0]][a[1]] = table[b[0]][b[1]]
        table[b[0]][b[1]] = 0

    la = downOrder[-1]
    table[la[0]][la[1]] = 0
    for i in range(len(downOrder)-1, 0, -1):
        a, b = downOrder[i], downOrder[i - 1]
        table[a[0]][a[1]] = table[b[0]][b[1]]
        table[b[0]][b[1]] = 0

for _ in range(T):
    spread()
    clean()



result = 0
for i in range(R):
    for j in range(C):
        if table[i][j] > 0:
            result += table[i][j]

print(result)
