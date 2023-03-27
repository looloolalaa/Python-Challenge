# 시뮬레이션
import heapq


class Player:
    def __init__(self, p, d, s):
        self.p = p
        self.d = d
        self.s = s
        self.gun = 0


n, m, k = map(int, input().split())
board = [list(map(lambda x: [-int(x)] if int(x) != 0 else [], input().split())) for _ in range(n)]
players = []
for _ in range(m):
    a, b, c, d = map(int, input().split())
    players.append(Player((a - 1, b - 1), c, -d))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def valid(p):
    return 0 <= p[0] < n and 0 <= p[1] < n


def go_one(player):
    pl = players[player]
    now, d = pl.p, pl.d
    next_p = now[0] + dx[d], now[1] + dy[d]
    if valid(next_p):
        pl.p = next_p
    else:
        d = (d + 2) % 4
        pl.p = now[0] + dx[d], now[1] + dy[d]
        pl.d = d


def exist_another_player(p):
    for i in range(m):
        if players[i].p == p:
            return True
    return False


def another_player(player):
    now = players[player].p
    for i in range(m):
        if i == player:
            continue
        if now == players[i].p:
            return i
    return -1


def get_gun(player):
    me = players[player]
    now = me.p
    if board[now[0]][now[1]]:
        strong_gun = heapq.heappop(board[now[0]][now[1]])
        if me.gun == 0:
            me.gun = strong_gun
        else:
            my_gun = me.gun
            me.gun = min(strong_gun, my_gun)
            heapq.heappush(board[now[0]][now[1]], max(strong_gun, my_gun))


scores = [0 for _ in range(m)]


def fight(a, b):
    player_a, player_b = players[a], players[b]
    total_a = player_a.s + player_a.gun
    total_b = player_b.s + player_b.gun

    winner, loser = -1, -1
    if total_a < total_b:
        winner, loser = a, b
    elif total_a > total_b:
        winner, loser = b, a
    else:
        winner, loser = (a, b) if player_a.s < player_b.s else (b, a)

    scores[winner] += abs(total_a - total_b)
    return winner, loser


def go_loser(player):
    me = players[player]
    now, d = me.p, me.d
    if me.gun != 0:
        heapq.heappush(board[now[0]][now[1]], me.gun)
        me.gun = 0

    next_p = now[0] + dx[d], now[1] + dy[d]
    while not valid(next_p) or exist_another_player(next_p):
        d = (d + 1) % 4
        me.d = d
        next_p = now[0] + dx[d], now[1] + dy[d]
    me.p = next_p
    get_gun(player)


def get_gun_winner(player):
    get_gun(player)


# go_one(0)
# get_gun(0)
# go_one(1)
# w, l = fight(1, another_player(1))
# go_loser(l)
# get_gun_winner(w)


def go(player):
    go_one(player)
    fighter = another_player(player)
    if fighter == -1:
        get_gun(player)
    else:
        winner, loser = fight(player, fighter)
        go_loser(loser)
        get_gun_winner(winner)


def simulate():
    for i in range(m):
        go(i)


# simulate()
# simulate()
# print(scores)
# for i in range(m):
#     print(players[i].p, players[i].gun)

# for b in board:
#     print(b)

for _ in range(k):
    simulate()
print(*scores)