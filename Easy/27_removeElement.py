def removeElement(nums=[1,2,3,3], val=3):
    diff = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[diff] = nums[i]
            diff += 1
    return diff,nums

print(removeElement())
