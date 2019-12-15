def twoSumBruteforce(nums=[3,2,4], target=6):
    for key, value in enumerate(nums):
        for key2, value2 in enumerate(nums):
            if value + value2 == target:
                if key2 > key:
                    return [key, key2]
def twoSum_fixOne(nums=[3,2,4], target=6):
    for key, value in enumerate(nums):
        diff=target-value
        if diff in nums:
            if key ==nums.index(diff):
                continue
            else:
                return [key, nums.index(diff)]
def twoSum_OnePass(nums=[3,2,4], target=6):
    seen={}
    for key, value in enumerate(nums):
        diff=target-value
        if diff in seen:
            return [seen[diff],key]
        seen[value]=key
    return []

print(twoSum_OnePass())