"""
bin(24 | 13)[2:]
'123'.rjust(10, '0')
-> '0000000123'
"""


def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        row = bin(a | b)[2:].rjust(n, '0')
        row = row.replace('1', '#')
        row = row.replace('0', ' ')
        answer.append(row)
    return answer


if __name__ == '__main__':
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))