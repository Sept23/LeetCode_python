def arrayPairSum(nums=[1,4,3,2]):
    sum = 0
    nums.sort()
    for k, v in enumerate(nums):
        if k % 2 == 0:
            sum += v
    return sum
print(arrayPairSum())