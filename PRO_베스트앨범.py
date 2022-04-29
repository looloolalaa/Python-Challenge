"""
temp.sort(key=lambda x: -f(x))
"""
from collections import defaultdict


def solution(genres, plays):
    book = defaultdict(list)
    for i in range(len(genres)):
        book[genres[i]].append(i)
    for k in book:
        book[k].sort(key=lambda x: -plays[x])

    count = []
    for k, v in book.items():
        count.append((k, sum(list(map(lambda x: plays[x], v)))))
    count.sort(key=lambda x: -x[1])

    result = []
    for g, c in count:
        result.extend(book[g][:2])
    return result


if __name__ == '__main__':
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))