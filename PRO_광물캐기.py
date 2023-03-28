# greedy
def solution(picks, minerals):
    s = sum(picks)
    minerals = minerals[:5 * s]

    priority = []
    for i in range(s):
        if 5 * i >= len(minerals):
            break
        temp = [0, 0, 0]
        for e in minerals[5 * i: 5 * (i + 1)]:
            if e == 'diamond':
                temp[0] += 1
            elif e == 'iron':
                temp[1] += 1
            elif e == 'stone':
                temp[2] += 1
        priority.append(temp)

    table = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]

    result = 0
    priority.sort(reverse=True)
    for p in priority:
        for i in range(3):
            if picks[i] != 0:
                picks[i] -= 1
                # i = 1
                # p = [3,2,0]
                tired = 0
                for j in range(3):
                    tired += table[i][j] * p[j]
                result += tired
                break

    return result

# [3,4,3]  __________


if __name__ == '__main__':
    print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))