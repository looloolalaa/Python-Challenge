"""
array[i] == array[i]로 끝나는 애들 모두 저장 j: [0~i-1]
"""

if __name__ == '__main__':
    N = int(input())
    array = list(map(int, input().split()))

    seq = [[array[0]]]

    for i in range(1, len(array)):
        max_len = -float('inf')
        max_idx = -1
        for j in range(i):
            if seq[j][-1] < array[i] and max_len < len(seq[j]):
                max_len = len(seq[j])
                max_idx = j

        if max_idx == -1:
            seq.append([array[i]])
        else:
            found = seq[max_idx][:]
            found.append(array[i])
            seq.append(found)


    max_len = -float('inf')
    max_idx = -1
    for i, s in enumerate(seq):
        if max_len < len(s):
            max_len = len(s)
            max_idx = i

    print(max_len)
    for s in seq[max_idx]:
        print(s, end=' ')