n = 5
table = [[-1 for _ in range(n)] for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


# 기본형
# now = n//2, n//2
# count = 0
# d = 0
# while valid(now):
#     if d % 2 == 0:
#         count += 1
#     for _ in range(count):
#         table[now[0]][now[1]] = d
#         now = now[0]+dx[d], now[1]+dy[d]
#         if not valid(now):
#             break
#     d = (d+1) % 4


# 반대방향까지
rev = [[-1 for _ in range(n)] for _ in range(n)]
now = n//2, n//2
count = 0
d = 0
while now != (0, n-1):
    if d % 2 == 0:
        count += 1
    for _ in range(count):
        table[now[0]][now[1]] = d
        now = now[0]+dx[d], now[1]+dy[d]
        rev[now[0]][now[1]] = (d + 2) % 4  # 다음 좌표에서 이전 좌표로 다시 돌아오는 방향
        if now == (0, n-1):
            break
    d = (d+1) % 4



for t in table:
    print(t)

print()
for r in rev:
    print(r)



