def moveZeroes(nums=[0,1,0,3,12]):
    """
    Do not return anything, modify nums in-place instead.
    """

    for i in range(len(nums)-1):
        if nums[i] == 0:
            for j in range(i + 1, len(nums)):
                if nums[j]!=0:
                    nums[i]=nums[j]
                    nums[j]=0
                    break
    return nums
print(moveZeroes())