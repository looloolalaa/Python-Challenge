from collections import Counter


def solution(participant, completion):
    person = Counter(participant) - Counter(completion)
    return list(person.keys())[0]


if __name__ == '__main__':
    print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))