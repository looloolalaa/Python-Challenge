"""
5
4 1 5 2 3
5
1 3 7 9 5
"""

if __name__ == '__main__':
    N = int(input())
    array = list(map(int, input().split()))
    M = int(input())
    wanted = list(map(int, input().split()))

    def isExist(k):
        left, right = 0, len(array)-1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == k:
                return True
            elif array[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        return False


    array.sort()
    answer = []
    for m in wanted:
        if isExist(m):
            answer.append(1)
        else:
            answer.append(0)

    for ans in answer:
        print(ans)
    # [1, 1, 0, 0, 1]
