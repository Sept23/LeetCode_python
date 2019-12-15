def removeDuplicates(nums=[0,0,0,1,1,2,3,4,5]):
    diff = 1
    if nums == []:
        return 0
    for i in range(len(nums)):
        if (i + 1 < len(nums)):
            if nums[i] < nums[i + 1]:
                nums[diff] = nums[i + 1]
                diff += 1
    return diff


print(removeDuplicates())