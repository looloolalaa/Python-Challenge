# n! == nPn
from itertools import permutations


def solution(k, dungeons):
    def can_go(k, dung):
        count = 0
        for mi, x in dung:
            if mi > k:
                return count
            else:
                k -= x
                count += 1
        return count

    candis = list(permutations(dungeons, len(dungeons)))
    return max(can_go(k, c) for c in candis)


if __name__ == '__main__':
    print(solution(80, [[80,20],[50,40],[30,10]]))