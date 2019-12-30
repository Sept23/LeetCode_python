def findMaxConsecutiveOnes(nums=[1,0,1,1,0,0]):
    # if len(nums)==1:
    #     return nums[0]
    maxSum = 0
    temp = 0
    for i in nums:
        if i == 1:
            temp += 1
            if temp > maxSum:
                maxSum = temp
        else:
            temp = 0
    return maxSum
print(findMaxConsecutiveOnes())