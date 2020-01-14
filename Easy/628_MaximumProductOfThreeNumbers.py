def maximumProduct( nums=[1,2,3]):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

print(maximumProduct())