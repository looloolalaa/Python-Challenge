# 좌표 2배 늘리기 (0.5초)
from collections import defaultdict

results = []
T = int(input())
for _ in range(T):

    N = int(input())
    atoms = {}
    for i in range(N):
        x, y, d, K = map(int, input().split())
        atoms[i] = [2*x, 2*y, d, K]

    dxy = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    next_pos = defaultdict(list)
    def get_next_pos():
        next_pos.clear()
        for i in atoms:
            x, y, d, k = atoms[i]
            next_p = (x+dxy[d][0], y+dxy[d][1])
            next_pos[next_p].append(i)


    result = 0
    def touch():
        global result
        for next_p in next_pos:
            if len(next_pos[next_p]) == 1:
                i = next_pos[next_p][0]
                atoms[i][0], atoms[i][1] = next_p[0], next_p[1]
            elif len(next_pos[next_p]) > 1:
                for meet in next_pos[next_p]:
                    result += atoms[meet][3]
                    atoms.pop(meet)
            else:
                print('error')

    # 4000
    for time in range(4002):
        get_next_pos()
        touch()

    # for a in atoms:
    #     print(a, atoms[a])
    results.append(result)

for t in range(T):
    print('#{} {}'.format(t+1, results[t]))