# 이동 구현: 스택 (한번 합쳐진 놈은 1로 마킹)
from itertools import product

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

result = 0
for p in list(product([0, 1, 2, 3], repeat=5)):
    new_table = [line[:] for line in table]

    def move(d):
        if d == 0:
            for i in range(N):
                stack = []
                for j in range(N):
                    if new_table[i][j] != 0:
                        if not stack or stack[-1][0] != new_table[i][j]:
                            stack.append((new_table[i][j], 0))
                            new_table[i][j] = 0
                        else:
                            if stack[-1][1] == 1:
                                stack.append((new_table[i][j], 0))
                                new_table[i][j] = 0
                            else:
                                val = stack.pop()[0]
                                stack.append((2*val, 1))
                                new_table[i][j] = 0

                for k in range(len(stack)):
                    new_table[i][k] = stack[k][0]

        elif d == 1:
            for i in range(N):
                stack = []
                for j in range(N-1, -1, -1):
                    if new_table[i][j] != 0:
                        if not stack or stack[-1][0] != new_table[i][j]:
                            stack.append((new_table[i][j], 0))
                            new_table[i][j] = 0
                        else:
                            if stack[-1][1] == 1:
                                stack.append((new_table[i][j], 0))
                                new_table[i][j] = 0
                            else:
                                val = stack.pop()[0]
                                stack.append((2 * val, 1))
                                new_table[i][j] = 0

                for k in range(len(stack)):
                    new_table[i][N-k-1] = stack[k][0]

        elif d == 2:
            for j in range(N):
                stack = []
                for i in range(N):
                    if new_table[i][j] != 0:
                        if not stack or stack[-1][0] != new_table[i][j]:
                            stack.append((new_table[i][j], 0))
                            new_table[i][j] = 0
                        else:
                            if stack[-1][1] == 1:
                                stack.append((new_table[i][j], 0))
                                new_table[i][j] = 0
                            else:
                                val = stack.pop()[0]
                                stack.append((2 * val, 1))
                                new_table[i][j] = 0

                for k in range(len(stack)):
                    new_table[k][j] = stack[k][0]

        elif d == 3:
            for j in range(N):
                stack = []
                for i in range(N-1, -1, -1):
                    if new_table[i][j] != 0:
                        if not stack or stack[-1][0] != new_table[i][j]:
                            stack.append((new_table[i][j], 0))
                            new_table[i][j] = 0
                        else:
                            if stack[-1][1] == 1:
                                stack.append((new_table[i][j], 0))
                                new_table[i][j] = 0
                            else:
                                val = stack.pop()[0]
                                stack.append((2 * val, 1))
                                new_table[i][j] = 0

                for k in range(len(stack)):
                    new_table[N-k-1][j] = stack[k][0]

    for d in p:
        move(d)

    # print(p)
    # for line in new_table:
    #     print(line)
    # print()

    for i in range(N):
        for j in range(N):
            result = max(result, new_table[i][j])

print(result)
