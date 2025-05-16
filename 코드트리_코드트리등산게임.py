# 최장증가부분수열(LIS) 응용
from bisect import bisect_left

Q = int(input())
line = list(map(int, input().split()))
n = line[1]
arr = line[2:]

temp = [0]
update_idx = [0]
stack = [[0]]
maxi = [[0]]


def plus(h):
    p = bisect_left(temp, h)
    update_idx.append(p)
    if p == len(temp):
        temp.append(h)
        stack.append([h])
        maxi.append([h])
    else:
        temp[p] = min(temp[p], h)
        stack[p].append(h)
        maxi[p].append(max(maxi[p][-1], h))


def minus():
    p = update_idx.pop()
    stack[p].pop()
    if not stack[p]:
        stack.pop()
        temp.pop()
        maxi.pop()
    else:
        temp[p] = stack[p][-1]
        maxi[p].pop()


for h in arr:
    plus(h)

for _ in range(Q - 1):
    inp = list(map(int, input().split()))
    if inp[0] == 200:
        h = inp[1]
        plus(h)
    elif inp[0] == 300:
        minus()
    elif inp[0] == 400:
        m_index = inp[1]

        car = update_idx[m_index]
        hiking = len(temp)
        print(100_0000 * (car + hiking - 2) + maxi[-1][-1])

# print(temp)
# print(update_idx)
# print(stack)
# print(maxi)

# 3 2 5 7 8 5 3 1 10 8   9
# 323
# 03

#   [3,2]   [10]
# 0 1 3 7 8 10
#   [2,1] [5,5,3][7][8,8]

# 0124

