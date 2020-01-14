def findLengthOfLCIS(nums=[]):
    length=len(nums)
    if length==0:
        return 0
    res = 1
    maxNum = -1
    for key, val in enumerate(nums):
        if key < length - 1:
            if nums[key + 1] > val:
                res += 1
                # print(maxNum," ",res)
            else:
                maxNum = max(maxNum, res)
                res = 1
        else:
            maxNum = max(maxNum, res)
    return maxNum

print(findLengthOfLCIS())