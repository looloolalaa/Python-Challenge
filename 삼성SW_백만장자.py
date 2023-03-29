# 주식
from collections import deque

def main():
    N = int(input())
    datas = list(map(int, input().split()))
    datas = deque(datas)

    result = 0
    while datas:
        max_value = max(datas)
        maxi = datas.index(max_value)
        for _ in range(maxi + 1):
            popped = datas.popleft()
            result += max_value - popped


    # print(result)
    results.append(result)


# main()
T = int(input())
results = []
for _ in range(T):
    main()

for i in range(T):
    print('#{} {}'.format(i+1, results[i]))
