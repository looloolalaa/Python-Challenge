"""
5 8 4
2 4 5 4 6
"""

if __name__ == '__main__':

    N, M, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    first_big = max(numbers)
    numbers.remove(first_big)
    second_big = max(numbers)

    result = 0
    line = [first_big for _ in range(K)]
    line.append(second_big)
    # [6, 6, 6, 6, 5]
    line_sum = sum(line)
    # 29
    line_count = M // (K + 1)
    result += line_sum * line_count
    result += sum(line[:(M % (K + 1))])

    print(result)

