"""
pattern 1~3
temp[i%len(temp)]
"""


def solution(answers):
    scores = [0, 0, 0]

    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, a in enumerate(answers):
        if a == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if a == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if a == pattern3[i % len(pattern3)]:
            scores[2] += 1

    max_score = max(scores)

    return [i + 1 for i, s in enumerate(scores) if s == max_score]


if __name__ == '__main__':
    print(solution([1,3,2,4,2]))