# 더블링크드 리스트 class 구현 시간초과
from math import floor

q = int(input())
line = list(map(int, input().split()))
n, m = line[1], line[2]
boxes = line[3:]
pos = [0 for _ in range(m + 1)]
# [1,2,2,2,1,4]

query = [list(map(int, input().split())) for _ in range(q - 1)]


class Node:
    def __init__(self, data):
        self.data = data
        self.before = None
        self.after = None


class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def empty(self):
        return self.head == None and self.tail == None

    def append(self, node):
        if self.empty():
            self.head = node
            self.tail = node
        else:
            node.tail = None
            self.tail.after = node
            node.before = self.tail
            self.tail = node
        self.count += 1

    def prepend(self, node):
        if self.empty():
            self.head = node
            self.tail = node
        else:
            node.before = None
            self.head.before = node
            node.after = self.head
            self.head = node
        self.count += 1

    def move_all_to(self, dlist):
        if self.empty():
            return dlist.count

        if dlist.empty():
            dlist.head = self.head
            dlist.tail = self.tail
        else:
            dlist.head.before = self.tail
            self.tail.after = dlist.head
            dlist.head = self.head
        self.head = self.tail = None

        dlist.count += self.count
        self.count = 0
        return dlist.count

    def give_front(self, dlist):
        if self.empty():
            return

        dlist.prepend(Node(self.head.data))
        if self.count >= 2:
            self.head = self.head.after
            self.head.before = None
        else:
            self.head = None
            self.tail = None
        self.count -= 1

    def change_front(self, dlist):
        if not self.empty() and not dlist.empty():
            self.head.data, dlist.head.data = dlist.head.data, self.head.data
        else:
            em, ex = (self, dlist) if self.empty() else (dlist, self)
            ex.give_front(em)

        return dlist.count

    def divide(self, dlist):
        if self.count <= 1:
            return dlist.count

        k = floor(self.count / 2)
        temp = DList()
        for _ in range(k):
            self.give_front(temp)

        for _ in range(k):
            temp.give_front(dlist)

        # target = self.head
        # for _ in range(k - 1):
        #     target = target.after

        # self.head = target.after
        # self.head.before = None

        # if dlist.empty():
        #     dlist.head = dlist.tail = target
        #     target.after = None
        # else:
        #     dlist.head.before = target
        #     target.after = dlist.head

        # while dlist.head.before != None:
        #     dlist.head = dlist.head.before

        # self.count -= k
        # dlist.count += k
        return dlist.count

    def get_info(self):
        a = self.head.data if self.head != None else -1
        b = self.tail.data if self.tail != None else -1
        c = self.count
        return a + 2 * b + 3 * c

    def show(self):
        p = self.tail
        while p != None:
            print(p.data, end=' ')
            p = p.before


def find(p_num):
    for belt in belts:
        if belt.empty():
            continue

        p = belt.head
        while p != None:
            if p.data == p_num:
                a = p.before.data if p.before != None else -1
                b = p.after.data if p.after != None else -1
                # print('**', a, p.data, b)
                return a + 2 * b
            p = p.after

    return 0


belts = [DList() for _ in range(n)]
for i in range(m):
    belts[boxes[i] - 1].append(Node(i + 1))

# belts[1].move_all_to(belts[3])
# belts[0].change_front(belts[3])
# belts[3].divide(belts[1])
# find(5)
# print(belts[2].get_info())

# for belt in belts:
#     belt.show()
#     print(':', belt.count)

result = []
for q in query:
    # print('--')
    # for belt in belts:
    #     belt.show()
    #     print(':', belt.count)
    if q[0] == 200:
        m_src, m_dst = q[1] - 1, q[2] - 1
        res = belts[m_src].move_all_to(belts[m_dst])
        result.append(res)
    elif q[0] == 300:
        m_src, m_dst = q[1] - 1, q[2] - 1
        res = belts[m_src].change_front(belts[m_dst])
        result.append(res)
    elif q[0] == 400:
        m_src, m_dst = q[1] - 1, q[2] - 1
        res = belts[m_src].divide(belts[m_dst])
        result.append(res)
    elif q[0] == 500:
        p_num = q[1]
        res = find(p_num)
        result.append(res)
    elif q[0] == 600:
        b_num = q[1] - 1
        res = belts[b_num].get_info()
        result.append(res)

for r in result:
    print(r)