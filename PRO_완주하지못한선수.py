"""
O: Counter +- Counter
X: Dict +- Dict instead Dict.update(Dict)
"""


from collections import Counter


def solution(participant, completion):
    person = Counter(participant) - Counter(completion)
    for p in person:
        return p
    return -1


if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))