if __name__ == '__main__':
    A, P = map(int, input().split())
    D = [A]
    s = {A}

    while True:
        next_val = 0
        for c in str(D[-1]):
            next_val += int(c)**P

        if next_val in s:
            print(D.index(next_val))
            break
        D.append(next_val)
        s.add(next_val)
