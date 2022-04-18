"""
Binary Search
"""

if __name__ == '__main__':
    k, n = map(int, input().split())
    array = [int(input()) for _ in range(k)]

    def total_count(m):
        count = [t//m for t in array]
        return sum(count)

    maxi = max(array)
    left, right = 1, maxi
    while left <= right:
        mid = (left + right) // 2
        if n > total_count(mid):
            right = mid - 1
        else:
            left = mid + 1
    print(right)


