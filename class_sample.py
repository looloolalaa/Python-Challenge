class Que:
    def __init__(self):
        self.que = []
        self.temp = 4444

    def push(self, item):
        self.que.append(item)

    def pop(self):
        return self.que.pop(0)

    def empty(self):
        return True if not self.que else False

    def change(self):
        self.temp = 100

    def show(self):
        print(self.temp)


if __name__ == '__main__':
    q = Que()
    q.temp = -1
    q.show()