def missingNumber(nums=[1]):
    maxNum = len(nums)
    groundtruth = set(range(0, maxNum + 1))
    numsSet = set(nums)
    result=list(groundtruth-numsSet)
    return result[0]

def missingNumber(nums=[1]):
        s = set(nums)
        for i in range(len(nums) + 1):
            if i in s:
                continue
            else:
                return i

print(missingNumber())