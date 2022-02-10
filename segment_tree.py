import sys

if __name__ == '__main__':
    # A = [4, 5, 8, 6, 1, 1, 0, 2, 14, 9]
    # tree = [0 for _ in range(4 * len(a))]


    # 세그먼트 트리 생성
    def init_tree():
        init_node(1, 0, len(A) - 1)

    def init_node(node, start, end):
        if start == end:
            tree[node] = A[start]
            return tree[node]
        else:
            mid = (start + end) // 2
            tree[node] = init_node(2 * node, start, mid) + init_node(2 * node + 1, mid + 1, end)
            return tree[node]

    # 구간 합 구하기
    def sum_sec(left, right):
        return sum_node(1, 0, len(A) - 1, left, right)

    def sum_node(node, start, end, left, right):
        if right < start or end < left:
            return 0
        elif left <= start and end <= right:
            return tree[node]
        else:
            mid = (start + end) // 2
            return sum_node(2 * node, start, mid, left, right) + sum_node(2 * node + 1, mid+1, end, left, right)

    # 배열 요소 변경
    def update_arr(idx, val):
        diff = val - A[idx]
        A[idx] = val
        update_node(1, 0, len(A) - 1, idx, diff)

    def update_node(node, start, end, idx, diff):
        if idx < start or end < idx:
            return
        else:
            tree[node] += diff
            if start != end:
                mid = (start+end)//2
                update_node(2*node, start, mid, idx, diff)
                update_node(2*node+1, mid+1, end, idx, diff)

    # init_tree()
    # print(sum_sec(5, 8))
    # update_arr(5, 400)
    # print(sum_sec(5, 8))

    N, M, K = map(int, input().split())
    A = [int(sys.stdin.readline()) for _ in range(N)]

    tree = [0 for _ in range(4 * len(A))]
    init_tree()

    answer = []
    for _ in range(M + K):
        a, b, c = map(int, sys.stdin.readline().split())
        if a == 1:
            update_arr(b-1, c)
        elif a == 2:
            answer.append(sum_sec(b-1, c-1))
        else:
            print('error')
            break

    for ans in answer:
        print(ans)