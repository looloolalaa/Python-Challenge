# board bfs
from collections import deque

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def valid(p):
    return 0<=p[0]<3 and 0<=p[1]<3

def clicked(boa, idx):
    b = [list(line) for line in boa]
    i, j = idx // 3, idx % 3
    b[i][j] = (1 if b[i][j] == 0 else 0)
    for d in dxy:
        a = i+d[0], j+d[1]
        if valid(a):
            b[a[0]][a[1]] = (1 if b[a[0]][a[1]] == 0 else 0)

    return tuple(tuple(l) for l in b)

book = {}
initial = ((0,0,0), (0,0,0), (0,0,0))
que = deque([(initial, 0)])
while que:
    board, cnt = que.popleft()
    if board in book:
        continue
    book[board] = cnt

    for idx in range(9):
        que.append((clicked(board, idx), cnt + 1))

for _ in range(int(input())):
    board = tuple(tuple(1 if c == '*' else 0 for c in input()) for _ in range(3))
    print(book[board])
