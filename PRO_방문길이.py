# xy set
def solution(dirs):
    n = 11
    p = (5, 5)
    dxy = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

    visited = set()
    for d in dirs:
        np = (p[0] + dxy[d][0], p[1] + dxy[d][1])
        if 0 <= np[0] < n and 0 <= np[1] < n:
            visited.add((p, np))
            visited.add((np, p))
            p = np

    return len(visited) // 2


if __name__ == '__main__':
    print(solution("ULURRDLLU"))