from collections import defaultdict


def solution(sales, links):
    tree = defaultdict(set)
    for p, c in links:
        tree[p].add(c)

    mini = {}

    def two_min(n):
        if n in mini:
            return mini[n]
        if n not in tree:
            return [0, sales[n-1]]
        sum_child = sum(min(two_min(child)) for child in tree[n])
        first_min = min(sum_child - min(two_min(child)) + two_min(child)[1] for child in tree[n])
        second_min = sales[n-1] + sum_child
        mini[n] = [first_min, second_min]
        return mini[n]

    return min(two_min(1))


if __name__ == '__main__':
    print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))