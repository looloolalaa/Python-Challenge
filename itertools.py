import itertools
if __name__ == '__main__':
    target = [1, 2, 3]
    print(list(itertools.combinations(target, 2)))
    print(list(itertools.permutations(target, 2)))
    print(list(itertools.product(target, repeat=2)))
    print(list(itertools.combinations_with_replacement(target, 2)))