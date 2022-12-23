# 더블 링크드 리스트
# 삽입 삭제 다수
def solution(n, k, cmd):
    class Node:
        def __init__(self, key):
            self.key = key
            self.prev = None
            self.next = None

    head = Node(-1)
    tail, start = head, head
    for i in range(n + 1):
        node = Node(i)
        tail.next = node
        node.prev = tail
        tail = tail.next

    for _ in range(k + 1):
        head = head.next

    stack = []
    for cm in cmd:
        c = cm[0]
        if c == 'U':
            move = int(cm.split()[1])
            for _ in range(move):
                head = head.prev

        elif c == 'D':
            move = int(cm.split()[1])
            for _ in range(move):
                head = head.next

        elif c == 'C':
            stack.append(head)
            head.prev.next = head.next
            head.next.prev = head.prev
            head = head.next if head.next.next != None else head.prev

        elif c == 'Z':
            back = stack.pop()
            back.prev.next = back
            back.next.prev = back

    remain = ['X' for _ in range(n)]
    while start != None:
        r = start.key
        if r != -1 and r != n:
            remain[r] = 'O'
        start = start.next

    return ''.join(remain)


if __name__ == '__main__':
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))