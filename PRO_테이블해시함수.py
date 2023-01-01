# sort by two factors
def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    result = 0
    for i in range(row_begin, row_end + 1):
        result ^= sum(d % i for d in data[i - 1])
    return result


if __name__ == '__main__':
    print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))