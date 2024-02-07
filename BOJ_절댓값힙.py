# heap __lt__
import heapq
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, num):
        self.num = num

    def __lt__(self, other):
        return (abs(self.num), self.num) < (abs(other.num), other.num)

h = []
result = []

N = int(input())
for _ in range(N):
    k = int(input())
    if k == 0:
        if not h:
            result.append(0)
        else:
            node = heapq.heappop(h)
            result.append(node.num)
    else:
        heapq.heappush(h, Node(k))

for r in result:
    print(r)

