def searchInsert(nums=[1,3,5,6], target=2):
    key = None
    if target in nums:
        key = nums.index(target)
    else:
        for k, v in enumerate(nums):
            if target < v:
                key = k
                break
    if key == None:
        key = len(nums)
    return key
print(searchInsert())