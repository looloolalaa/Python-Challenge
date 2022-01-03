def minPatches(nums, n):
    count = 0
    i, upto = 0, 0
    N = len(nums)
    while upto<n:
        if i<N and nums[i]<=upto+1:
            upto += nums[i]
            i+=1
        else:
            count+=1
            upto+=(upto+1)

    return count


if __name__ == '__main__':
    nums = [1,2,2]
    n = 5
    print(minPatches(nums, n))