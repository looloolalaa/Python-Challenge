"""
j == [i+1:] check
"""


def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        j = -1
        for j in range(i + 1, len(prices)):
            if prices[j] < prices[i]:
                break
        answer.append(j - i)
    answer.append(0)
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3]))