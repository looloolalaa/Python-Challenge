import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    A = [int(sys.stdin.readline()) for _ in range(N)]
    min_max_tree = [(0, 0) for _ in range(4 * len(A))]

    def init_min_max_tree():
        init_min_max_node(1, 0, len(A)-1)

    def init_min_max_node(node, start, end):
        if start == end:
            min_max_tree[node] = (A[start], A[start])
            return min_max_tree[node]
        else:
            mid = (start+end)//2
            left_child = init_min_max_node(2 * node, start, mid)
            right_child = init_min_max_node(2 * node + 1, mid + 1, end)
            min_max_tree[node] = (min(left_child[0], right_child[0]), max(left_child[1], right_child[1]))
            return min_max_tree[node]

    def get_min_max(left, right):
        return get_min_max_node(1, 0, len(A)-1, left, right)

    def get_min_max_node(node, start, end, left, right):
        if right < start or end < left:
            return float('inf'), -float('inf')
        elif left <= start and end <= right:
            return min_max_tree[node]
        else:
            mid = (start+end)//2
            left_child = get_min_max_node(2 * node, start, mid, left, right)
            right_child = get_min_max_node(2 * node + 1, mid + 1, end, left, right)
            return min(left_child[0], right_child[0]), max(left_child[1], right_child[1])


    init_min_max_tree()

    answer = []
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        answer.append(get_min_max(a - 1, b - 1))

    # print(min_max_tree)
    for mi, ma in answer:
        print(mi, ma)
