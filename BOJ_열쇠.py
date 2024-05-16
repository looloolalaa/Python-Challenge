# 문을 저장해두고 열쇠를 발견하면 그제서야 방문
# or 이미 열수있는 문이면 열고 지나가기
from collections import deque, defaultdict

for _ in range(int(input())):
    h, w = map(int, input().split())
    table = [['.' for _ in range(w+2)]]
    for _ in range(h):
        table.append(['.'] + list(input()) + ['.'])
    table.append(['.' for _ in range(w+2)])
    hold = set(input())

    def valid(p):
        return 0 <= p[0] < h+2 and 0 <= p[1] < w+2
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


    que = deque([(0, 0)])
    visited = [[False for _ in range(w+2)] for _ in range(h+2)]
    visited[0][0] = True

    def go(p):
        que.append(p)
        visited[p[0]][p[1]] = True
        table[p[0]][p[1]] = '.'

    def found_key(ch):
        hold.add(ch)
        for p in doors[ch.upper()]:
            go(p)

    ans = 0
    doors = defaultdict(list)

    while que:
        i, j = que.popleft()
        for d in dxy:
            a = i+d[0], j+d[1]
            if valid(a) and not visited[a[0]][a[1]]:
                val = table[a[0]][a[1]]
                if val == '.':
                    go(a)
                elif val == '$':
                    go(a)
                    ans += 1
                elif val.islower():
                    go(a)
                    found_key(val)
                elif val.isupper():
                    if val.lower() in hold:
                        go(a)
                    else:
                        doors[val].append(a)

    print(ans)
