# 케이스 고민
from itertools import product


N = input()
M = int(input())
wrong = set()
if M > 0:
    wrong = set(input().split())

nums = set(str(i) for i in range(10))
nums -= wrong

if not nums:
    print(abs(int(N) - 100))
    exit()

if nums == {'0'}:
    print(min(1 + int(N), abs(int(N) - 100)))
    exit()

mini = float('inf')
for p in product(nums, repeat=len(N)):
    mini = min(mini, abs(int(''.join(p)) - int(N)) + len(N))


up = min(nums - {'0'})
up += min(nums) * len(N)
mini = min(mini, len(up) + int(up) - int(N))


if len(N) > 1:
    down = max(nums) * (len(N)-1)
    mini = min(mini, int(N) - int(down) + len(N)-1)


print(min(mini, abs(int(N) - 100)))

