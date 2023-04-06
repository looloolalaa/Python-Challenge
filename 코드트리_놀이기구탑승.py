# 우선순위 튜플 가능
# (친구수, 빈칸수, -행, -열)
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
orders = [list(map(int, input().split())) for _ in range(n*n)]

scores = [[0 for _ in range(n)] for _ in range(n)]
max_score = 0

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def valid(p):
    return 0<=p[0]<n and 0<=p[1]<n

def get_scores(likes):
    global max_score
    max_score = 0
    for i in range(n):
        for j in range(n):
            scores[i][j] = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                score = 0
                for d in dxy:
                    a = i+d[0],j+d[1]
                    if valid(a) and board[a[0]][a[1]] in likes:
                        score += 1
                scores[i][j] = score
                max_score = max(max_score, score)

def get_seat():
    result = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and scores[i][j] == max_score:
                result.append((i, j))
    return result


def empty_count(p):
    count = 0
    for d in dxy:
        a = p[0]+d[0],p[1]+d[1]
        if valid(a) and board[a[0]][a[1]] == 0:
            count += 1
    return count


# board[1][1] = 3
# board[0][1] = 6
# board[0][0] = 1
# get_scores([1,2,3,4])
# candis = get_seat()
# max_empty_count = max(empty_count(can) for can in candis)

# for can in candis:
#     if empty_count(can) == max_empty_count:
#         print(can)
#         break

like = {}
for n0, n1, n2, n3, n4 in orders:
    like[n0] = [n1, n2, n3, n4]

    get_scores([n1, n2, n3, n4])
    seats = get_seat()
    if len(seats) > 1:
        max_empty_count = max(empty_count(seat) for seat in seats)
        p = -1, -1
        for seat in seats:
            if empty_count(seat) == max_empty_count:
                p = seat
                break
        board[p[0]][p[1]] = n0

    else:
        p = seats[0]
        board[p[0]][p[1]] = n0



sc = [0, 1, 10, 100, 1000]

result = 0
for i in range(n):
    for j in range(n):
        me = board[i][j]
        count = 0
        for d in dxy:
            a = i+d[0],j+d[1]
            if valid(a) and board[a[0]][a[1]] in like[me]:
                count += 1
        result += sc[count]

print(result)
# for b in board:
#     print(b)