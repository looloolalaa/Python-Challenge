# counting 배열로 늘리기
from collections import Counter

r, c, k = map(int, input().split())
table = [[0 for _ in range(100)] for _ in range(100)]
for i in range(3):
    line = list(map(int, input().split()))
    for j in range(3):
        table[i][j] = line[j]

n, m = 3, 3

def simulate():
    if n >= m:
        row()
    else:
        col()

def counting(arr):
    new_arr = list(Counter(arr).items())
    new_arr.sort(key=lambda x: (x[1], x[0]))

    result = []
    for a, c in new_arr:
        result.append(a)
        result.append(c)
    return result[:100]


def row():
    global m

    max_len = 0
    for i in range(n):
        nums = []
        for j in range(m):
            if table[i][j] != 0:
                nums.append(table[i][j])
                table[i][j] = 0

        new_nums = counting(nums)
        max_len = max(max_len, len(new_nums))
        for k in range(len(new_nums)):
            table[i][k] = new_nums[k]

    m = max_len

def col():
    global n

    max_len = 0
    for j in range(m):
        nums = []
        for i in range(n):
            if table[i][j] != 0:
                nums.append(table[i][j])
                table[i][j] = 0

        new_nums = counting(nums)
        max_len = max(max_len, len(new_nums))
        for k in range(len(new_nums)):
            table[k][j] = new_nums[k]

    n = max_len

# print(counting2([5,5,5]))

time = 0
while time <= 100:
    if table[r-1][c-1] == k:
        print(time)
        exit()

    simulate()
    time += 1

    # print(time, ':', n, m)
    # for t in table[:10]:
    #     print(t[:10])





print(-1)
