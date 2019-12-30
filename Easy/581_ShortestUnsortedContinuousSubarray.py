def findUnsortedSubarray(nums=[2,6,4,8,10,9,15]):
    nums_ = nums.copy()
    nums.sort()
    num = 0
    loc = []
    for k, v in enumerate(nums):
        if v != nums_[k]:
            num += 1
            loc.append(k)
    if len(loc) == 0:
        return 0
    else:
        return loc[-1] - loc[0] + 1
print(findUnsortedSubarray())