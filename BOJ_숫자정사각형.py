# 정사각형 대보기
N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(input())

def main():
    size = min(N, M)
    while size >= 1:
        for i in range(N-size+1):
            for j in range(M-size+1):
                if table[i][j] == table[i][j+size-1] == table[i+size-1][j] == table[i+size-1][j+size-1]:
                    return size * size
        size -= 1

    return -1


print(main())