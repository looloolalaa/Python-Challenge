# 트라이 트리 풀이
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

class Node:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}

trie = Node('-')
for _ in range(N):
    now = trie
    for c in input():
        if c not in now.children:
            new_node = Node(c)
            now.children[c] = new_node
        now = now.children[c]

ans = 0
for _ in range(M):
    now = trie
    for c in input().rstrip():
        if c not in now.children:
            break
        now = now.children[c]
    else:
        ans += 1

print(ans)