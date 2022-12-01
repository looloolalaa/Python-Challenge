if __name__ == '__main__':
    class Node:
        def __init__(self, key):
            self.key = key
            self.value = False  # data
            self.children = {}


    class Trie:
        def __init__(self):
            self.root = Node('')

        def insert_iter(self, s):
            now = self.root
            for c in s:
                if c not in now.children:
                    now.children[c] = Node(c)
                now = now.children[c]
            now.value = True

        def search_iter(self, s):
            now = self.root
            for c in s:
                if c not in now.children:
                    return False
                now = now.children[c]
            return now.value

        # recursion
        def insert(self, s):
            self.insert_node(self.root, s)

        def insert_node(self, r, s):
            if not s:
                r.value = True
                return
            if s[0] not in r.children:
                r.children[s[0]] = Node(s[0])
            self.insert_node(r.children[s[0]], s[1:])

        def search(self, s):
            return self.search_node(self.root, s)

        def search_node(self, r, s):
            if not s:
                if r.value:
                    return True
                else:
                    return False
            if s[0] not in r.children:
                return False
            return self.search_node(r.children[s[0]], s[1:])

        def print_leaf(self, r):
            if r.value:
                print(r.key)
            for child in r.children.values():
                self.print_leaf(child)


    data = ['to', 'tea', 'ted', 'ten', 'A', 'i', 'in', 'inn']
    # value = [7, 3, 4, 12, 15, 11, 5, 9]

    tree = Trie()
    for d in data:
        tree.insert_iter(d)

    print(tree.search_iter('in'))
