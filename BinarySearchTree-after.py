# all operations
if __name__ == '__main__':
    # data = [21, 28, 14, 32, 25, 18, 11, 30, 19, 15]
    data = [5, 2, 4, 22, 10, 12, 15, 60, 44, 9]


    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None


    class BSTree:
        def __init__(self):
            self.root = None

        def insert(self, key):
            if self.root is None:
                self.root = Node(key)
            else:
                self.insert_node(self.root, key)

        def insert_node(self, r, k):
            if k < r.key:
                if r.left is None:
                    r.left = Node(k)
                else:
                    self.insert_node(r.left, k)
            else:
                if r.right is None:
                    r.right = Node(k)
                else:
                    self.insert_node(r.right, k)

        def search(self, key):
            if self.root is None:
                return None
            else:
                return self.search_node(self.root, key)

        def search_node(self, r, k):
            if k < r.key:
                if r.left is None:
                    return False
                else:
                    return self.search_node(r.left, k)
            elif r.key < k:
                if r.right is None:
                    return False
                else:
                    return self.search_node(r.right, k)
            else:
                return True

        def delete(self, key):
            if self.root is None or not self.search(key):
                return None
            else:
                return self.delete_node(self.root, key)

        def delete_node(self, r, k):
            found_p, found = None, r
            while found.key != k:
                if k < found.key:
                    found_p, found = found, found.left
                elif found.key < k:
                    found_p, found = found, found.right

            # root
            if found_p is None:
                if found.left is None and found.right is None:
                    self.root = None
                elif found.left is None or found.right is None:
                    found_child = found.left
                    if found_child is None:
                        found_child = found.right
                    self.root = found_child
                else:
                    succ_p, succ = found, found.right
                    while succ.left is not None:
                        succ_p, succ = succ, succ.left
                    # print(found_p.key, found.key, succ_p.key, succ.key)
                    if found == succ_p:
                        succ_p.right = succ.right
                    else:
                        succ_p.left = succ.right
                    found.key, succ.key = succ.key, found.key  # data copy
                    found = succ

            else:  # not root
                if found.left is None and found.right is None:
                    if found_p.left == found:
                        found_p.left = None
                    elif found_p.right == found:
                        found_p.right = None

                # 2
                elif found.left is None or found.right is None:
                    found_child = found.left
                    if found_child is None:
                        found_child = found.right

                    if found_p.left == found:
                        found_p.left = found_child
                    elif found_p.right == found:
                        found_p.right = found_child

                # 3
                else:
                    succ_p, succ = found, found.right
                    while succ.left is not None:
                        succ_p, succ = succ, succ.left
                    # print(found_p.key, found.key, succ_p.key, succ.key)
                    if found == succ_p:
                        succ_p.right = succ.right
                    else:
                        succ_p.left = succ.right
                    found.key, succ.key = succ.key, found.key  # data copy
                    found = succ

            return found

        def print_tree(self):
            if self.root is None:
                print("Tree Empty..")
            else:
                self.inOrder(self.root)

        def inOrder(self, n):
            if n is None:
                return
            self.inOrder(n.left)
            print(n.key)
            self.inOrder(n.right)

    tree = BSTree()
    for d in data:
        tree.insert(d)

    print(tree.search(22))
    print(tree.search(61))
    print(tree.search(60))
    print(tree.delete(60))
    print(tree.search(60))
    print(tree.delete(22))
    print(tree.delete(44))
    print(tree.search(22))
    print(tree.search(44))

