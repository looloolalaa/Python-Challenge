import itertools

def solution(k, num, links):

    root = [i for i in range(len(num))]
    for link in links:
        if link[0] != -1:
            root.remove(link[0])
        if link[1] != -1:
            root.remove(link[1])
    root = root[0]

    edges = []
    for i, link in enumerate(links):
        if link[0] != -1:
            edges.append((i, link[0]))
        if link[1] != -1:
            edges.append((i, link[1]))

    cases = list(itertools.combinations(edges, k-1))

    def group_max(edges):
        group = []

        def sum_node(n):
            if n == -1:
                return 0

            left = links[n][0]
            right = links[n][1]
            if (n, left) in edges and (n, right) in edges:
                group.append(sum_node(left))
                group.append(sum_node(right))
                return num[n]
            elif (n, left) in edges:
                group.append(sum_node(left))
                return sum_node(right) + num[n]
            elif (n, right) in edges:
                group.append(sum_node(right))
                return sum_node(left) + num[n]
            else:
                return sum_node(left) + sum_node(right) + num[n]

        group.append(sum_node(root))
        return max(group)

    mini = float('inf')
    for case in cases:
        print(case)
        if mini > group_max(case):
            mini = group_max(case)

    return mini


if __name__ == '__main__':
    print(solution(3,[12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
                   [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))