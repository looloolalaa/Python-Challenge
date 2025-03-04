# 동점팀 진출 확률
def next_round_p(score):
    # [1,4,1,0]
    rank = [0,0,0,0]
    for i in range(4):
        big = 0
        for s in score:
            if s > score[i]:
                big += 1
        rank[i] = big

    # [1,0,1,3]
    rank0, rank1 = 0, 0
    for r in rank:
        if r == 0:
            rank0 += 1
        elif r == 1:
            rank1 += 1

    def prob(ra):
        if ra >= 2:
            return 0
        if ra == 0:
            if rank0 <= 2:
                return 1
            else:
                return 2 / rank0
        if ra == 1:
            return 1/rank1

    return [prob(r) for r in rank]

country = dict((c, i) for i, c in enumerate(input().split()))
# {'aa': 2}
lines = [list(input().split()) for _ in range(6)]
score = [0,0,0,0]

ans = [0,0,0,0]
def dfs(i, p):
    if p == 0:
        return

    if i == 6:
        res_pro = [pro * p for pro in next_round_p(score)]
        for k in range(4):
            ans[k] += res_pro[k]
        return

    line = lines[i]
    a, b = country[line[0]], country[line[1]]

    score[a] += 3
    dfs(i + 1, p * float(line[2]))
    score[a] -= 3

    score[a] += 1
    score[b] += 1
    dfs(i + 1, p * float(line[3]))
    score[b] -= 1
    score[a] -= 1

    score[b] += 3
    dfs(i + 1, p * float(line[4]))
    score[b] -= 3

dfs(0, 1)
for a in ans:
    print(a)

