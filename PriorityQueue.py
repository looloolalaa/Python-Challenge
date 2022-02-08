from queue import PriorityQueue

if __name__ == '__main__':
    que = PriorityQueue()
    que.put((4, 'middle'))
    que.put((5, 'five'))
    que.put((1, 'first'))
    que.put((8, 'low'))

    print(que.get())
    print(que.get())
    print(que.qsize())
    print(que.empty())
