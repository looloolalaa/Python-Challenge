from itertools import combinations


def solution(nums):
    result = 0

    def isPrime(n):
        if n == 1:
            return False
        return all(n % i != 0 for i in range(2, int(n**0.5)+1))

    nums = combinations(nums, 3)
    for a, b, c in nums:
        if isPrime(a + b + c):
            result += 1
    return result


if __name__ == '__main__':
    print(solution([1,2,7,6,4]))