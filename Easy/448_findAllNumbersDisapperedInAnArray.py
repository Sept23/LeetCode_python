def findDisappearedNumbers(nums=[4,3,2,7,8,2,3,1]) :
    numSet = range(1, len(nums) + 1)
    difference = list(set(numSet) - set(nums))
    return difference
print(findDisappearedNumbers())