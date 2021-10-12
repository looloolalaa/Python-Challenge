import itertools

def find_subset(atoms, case):
    for i, atom in enumerate(atoms):
        if atom <= case or atom >= case:
            return i
    return len(atoms)

def get_atoms(cases):
    atoms = [cases[0]]
    for case in cases:
        subset_index = find_subset(atoms, case)
        if subset_index >= len(atoms):
            atoms.append(case)
        else:
            found = atoms[subset_index]
            if found > case:
                atoms.remove(found)
                atoms.append(case)

    return atoms


def solution(sales, links):
    relation = {}
    for link in links:
        parent = link[0]
        child = link[1]
        if parent not in relation:
            relation[parent] = [child]
        else:
            relation[parent].append(child)

    belongs = list(relation.keys())
    belongs.remove(1)

    cases = []
    for parent, children in relation.items():
        case = [parent]
        case.extend(children)
        front = []
        rear = []
        for c in case:
            front.append(c) if c in belongs else rear.append(c)
        if rear:
            front.append(min(rear, key=lambda x: sales[x-1]))
        cases.append(front)

    print(relation)

    cases = list(itertools.product(*cases))
    cases = list(map(lambda x: set(x), cases))
    cases = get_atoms(cases)
    sale_cases = []
    for case in cases:
        sale = sum([sales[num - 1] for num in case])
        sale_cases.append(sale)

    # print(cases)
    return min(sale_cases)


if __name__ == '__main__':
    sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
    links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
    print(solution(sales, links))