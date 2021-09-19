# 첫 이상
def lower_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

# 첫 초과
def upper_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left+right)//2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return right


if __name__ == '__main__':
    numbers = [1,2,3,3,4,4,4,4]
    print(lower_bound(numbers, 3))
    print(upper_bound(numbers, 3))