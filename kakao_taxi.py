from math import inf

def solution(n, s, a, b, fares):
    answer = 0

    max_fare = inf
    s = s-1
    a = a-1
    b = b-1

    # init
    cost = []
    for i in range(n):
        temp = [max_fare for _ in range(n)]
        temp[i] = 0
        cost.append(temp)
    for fare in fares:
        cost[fare[0]-1][fare[1]-1] = fare[2]
        cost[fare[1] - 1][fare[0] - 1] = fare[2]

    # floyd
    for k in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    # for c in cost:
    #     print(c)

    via = []
    for i in range(n):
        via.append(cost[s][i] + cost[i][a] + cost[i][b])
    answer = min(via)

    # print(via)

    return answer


if __name__ == '__main__':
    print(solution(7,3,4,1,
                   [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
             ))