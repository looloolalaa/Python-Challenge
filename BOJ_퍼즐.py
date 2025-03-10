# BFS 상태 탐색
from collections import deque

aim = []
for _ in range(3):
    aim += list(map(int, input().split()))

around = [[1,3], [0,2,4], [1,5], [0,4,6], [1,3,5,7], [2,4,8], [3,7], [4,6,8], [5,7]]

visited = set()
que = deque([(0, [1,2,3, 4,5,6, 7,8,0], 8)])
while que:
    depth, board, zeroPos = que.popleft()
    if tuple(board) in visited:
        continue

    if board == aim:
        print(depth)
        exit(0)

    visited.add(tuple(board))

    for a in around[zeroPos]:
        newBoard = board[:]
        newBoard[zeroPos], newBoard[a] = newBoard[a], newBoard[zeroPos]

        que.append((depth+1, newBoard, a))

print(-1)