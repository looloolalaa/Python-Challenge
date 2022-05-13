"""
permu + prime
"""
from itertools import permutations


def solution(numbers):
    numbers = [num for num in numbers]
    possible = set()

    def isPrime(n):
        if n < 2:
            return False
        return all(n % i != 0 for i in range(2, int(n ** (1 / 2)) + 1))

    for i in range(1, len(numbers) + 1):
        possible.update(set(map(lambda x: int(''.join(x)), permutations(numbers, i))))

    count = 0
    for p in possible:
        if isPrime(p):
            count += 1
    return count


if __name__ == '__main__':
    # "011"
    print(solution("17"))