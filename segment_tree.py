if __name__ == '__main__':
    a = [4, 5, 8, 6, 1, 1, 0, 2, 14, 9]
    tree = [0 for _ in range(4 * len(a))]


    def init_tree():
        init(1, 0, len(a) - 1)

    def init(node, start, end):
        if start == end:
            tree[node] = a[start]
            return tree[node]
        else:
            mid = (start + end) // 2
            tree[node] = init(2 * node, start, mid) + init(2 * node + 1, mid + 1, end)
            return tree[node]

    def sum_sec(left, right):
        return sum_tree(1, 0, len(a) - 1, left, right)

    def sum_tree(node, start, end, left, right):
        if right < start or end < left:
            return 0
        elif left <= start and end <= right:
            return tree[node]
        else:
            mid = (start + end) // 2
            return sum_tree(2 * node, start, mid, left, right) + sum_tree(2 * node + 1, mid+1, end, left, right)

    def update_arr(idx, val):
        diff = val - a[idx]
        a[idx] = val
        update_tree(1, 0, len(a)-1, idx, diff)

    def update_tree(node, start, end, idx, diff):
        if idx < start or end < idx:
            return
        else:
            tree[node] += diff
            if start != end:
                mid = (start+end)//2
                update_tree(2*node, start, mid, idx, diff)
                update_tree(2*node+1, mid+1, end, idx, diff)

    init_tree()
    print(sum_sec(5, 8))
    update_arr(5, 400)
    print(sum_sec(5, 8))