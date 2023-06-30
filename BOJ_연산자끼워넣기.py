from itertools import combinations

# 경우 하나의 칸 개수로 dfs 생각하기
# N = 6
# nums = [1, 2, 3, 4, 5, 6]
# temp = [2, 1, 1, 1]
# # [0, 0, 1, 2, 3]
#
# ops = [-1 for _ in range(5)]
#
# count = 0
#
# def dfs(i):
#     if i == 5:
#         global count
#         print(ops, count)
#         count += 1
#         return
#
#     for j in range(4):
#         if temp[j] > 0:
#             ops[i] = j
#             temp[j] -= 1
#             dfs(i+1)
#             temp[j] += 1
#
# dfs(0)

N = int(input())
nums = list(map(int, input().split()))
temp = list(map(int, input().split()))


cards = set(i for i in range(N-1))
res = [-1 for _ in range(N-1)]
candis = []

for c in combinations(cards, temp[0]):
    for k in c:
        res[k] = 0
    remain = cards - set(c)
    for a in combinations(remain, temp[1]):
        for k in a:
            res[k] = 1
        rremain = remain - set(a)
        for b in combinations(rremain, temp[2]):
            for k in b:
                res[k] = 2
            rrremain = rremain - set(b)
            for d in combinations(rrremain, temp[3]):
                for k in d:
                    res[k] = 3
                candis.append(res[:])

# print(candis)
# cards = []
# for i in range(4):
#     for _ in range(temp[i]):
#         cards.append(i)

# candis = set()
# for p in permutations([i for i in range(N-1)], len(cards)):
#     pos = [-1 for _ in range(len(cards))]
#     for i in range(len(cards)):
#         pos[p[i]] = cards[i]
#
#     candis.add(tuple(pos))


def calc(c):
    # c = (0, 2, 0, 3, 1)
    res = nums[0]
    for i in range(N-1):
        if c[i] == 0:
            res += nums[i+1]
        elif c[i] == 1:
            res -= nums[i+1]
        elif c[i] == 2:
            res *= nums[i+1]
        elif c[i] == 3:
            if res < 0:
                res = -((-res) // nums[i+1])
            else:
                res //= nums[i+1]

    return res

mini = float('inf')
maxi = -float('inf')
for c in candis:
    val = calc(c)
    mini = min(mini, val)
    maxi = max(maxi, val)

print(maxi)
print(mini)





