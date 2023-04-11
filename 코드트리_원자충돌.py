# 둥근 격자 + 원자 클래스
# -> class 말고 tuple 로 가능
class Atom:
    def __init__(self, w, s, d):
        self.w = w
        self.s = s
        self.d = d


n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, w, s, d = map(int, input().split())
    board[x-1][y-1].append(Atom(w, s, d))


def simulate():
    go()
    meet()

dxy = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
def next_p(x, y, s, d):
    arrow = dxy[d]
    nx = (x + arrow[0]*s + n*s) % n
    ny = (y + arrow[1]*s + n*s) % n
    return nx, ny

def go():
    global board
    moved = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for atom in board[i][j]:
                np = next_p(i, j, atom.s, atom.d)
                moved[np[0]][np[1]].append(atom)

    board = moved


def meet():
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) < 2:
                continue

            total_w, total_s = 0, 0
            for atom in board[i][j]:
                total_w += atom.w
                total_s += atom.s

            new_d = -1
            if all(atom.d % 2 == 0 for atom in board[i][j]) or all(atom.d % 2 == 1 for atom in board[i][j]):
                new_d = 0
            else:
                new_d = 1

            mini_w, mini_s = int(total_w / 5), int(total_s / len(board[i][j]))
            board[i][j] = []
            if mini_w == 0:
                continue

            for _ in range(4):
                board[i][j].append(Atom(mini_w, mini_s, new_d))
                new_d = (new_d + 2) % 8


for _ in range(k):
    simulate()

result = 0
for i in range(n):
    for j in range(n):
        for atom in board[i][j]:
            result += atom.w

print(result)