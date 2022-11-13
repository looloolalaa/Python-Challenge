# O(n + k) sort
# k: Maximum value
if __name__ == '__main__':
    data = [3, 6, 9, 2, 6, 7, 3, 5]

    # 전체 데이터 개수
    n = len(data)

    # 최대값을 찾는다.
    k = max(data)

    # 배열을 생성한다.
    table = [0] * (k + 1)

    # 각 원소가 등장하는 횟수를 구한다.
    for element in data:
        table[element] += 1

    # 해당 원소가 마지막으로 등장하는 위치를 구한다.
    for i in range(1, len(table)):
        table[i] += table[i - 1]
    sorted_array = [0] * n

    # 왜 거꾸로 참조할까요?
    for elem in reversed(data):
        # elem 의 위치는?
        sorted_array[table[elem] - 1] = elem

        # 왜 1 을 빼줄까요?
        table[elem] -= 1
    print(sorted_array)