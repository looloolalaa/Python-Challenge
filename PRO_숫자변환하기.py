# 최소 횟수 DP
def solution(x, y, n):
    counter = {x: 0}
    for i in range(x, y):
        if i in counter:
            counter[i + n] = min(counter[i + n] if i + n in counter else float('inf'), counter[i] + 1)
            counter[i * 2] = min(counter[i * 2] if i * 2 in counter else float('inf'), counter[i] + 1)
            counter[i * 3] = min(counter[i * 3] if i * 3 in counter else float('inf'), counter[i] + 1)

    return counter[y] if y in counter else -1


if __name__ == '__main__':
    print(solution(10, 40, 52))