# 2
# def gcd(a, b):
#     if a % b == 0:
#         return b
#     return gcd(b, a % b)
#
# n, m = map(int, input().split())
# print(gcd(n, m))


# 3
# n = int(input())
# table = [list(map(int, input().split())) for _ in range(n)]
# r, c = map(int, input().split())
# target = table[r-1][c-1]
#
# for i in range(r):
#     for j in range(c):
#         if table[i][j] < target:
#             table[i][j] = 0
#
# for t in table:
#     print(*t)

# 4
# from itertools import product
#
#
# n, k = map(int, input().split())
# for row in sorted(list(product([i+1 for i in range(n)], repeat=k)), reverse=True):
#     print(*row)

# 5
# n = int(input())
# table = [list(map(int, input().split())) for _ in range(n)]
#
# a = -1, -1
# b = -1, -1
# for i in range(n):
#     for j in range(n):
#         if table[i][j] == 2:
#             a = i, j
#         if table[i][j] == 3:
#             b = i, j
#
#
# def valid(p):
#     return 0 <= p[0] < n and 0 <= p[1] < n
#
#
# dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#
#
# def size(p):
#     if table[p[0]][p[1]] == 0:
#         return 0
#
#     s = 1
#     table[p[0]][p[1]] = 0
#     for d in dxy:
#         a = p[0] + d[0], p[1] + d[1]
#         if valid(a):
#             s += size(a)
#     return s
#
#
# print(size(a), size(b))



# 6
# n = int(input())
# table = [[0 for _ in range(n+1)] for _ in range(n+1)]
#
# for i in range(n):
#     table[i][1:] = list(map(int, input().split()))
#
# for i in range(n-1, -1, -1):
#     for j in range(1, n+1):
#         table[i][j] += max(table[i][j-1], table[i+1][j])
#
# print(table[0][-1])


# 7
# from collections import Counter
# n, k = map(int, input().split())
# cards = list(map(int, input().split()))
#
# ans = 0
# counter = Counter()
# for card in cards:
#     div = k / card
#     ans += counter[div]
#     counter[card] += 1
#
# print(ans)


# 8
# n, a, b = map(int, input().split())
# arr = list(map(int, input().split()))
#
# x, y = 0, 0
# s = arr[0]
#
# dist = float('inf')
# while x < n:
#     if a <= s <= b:
#         dist = min(dist, y-x+1)
#         s -= arr[x]
#         x += 1
#
#     elif s < a:
#         y += 1
#         if y >= n:
#             break
#         s += arr[y]
#     elif s > b:
#         s -= arr[x]
#         x += 1
#
# print(dist if dist != float('inf') else -1)
