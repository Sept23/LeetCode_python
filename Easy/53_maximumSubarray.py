import time
def maxSubArray( nums=[5,-1,4]):
    maxNum = None
    solutions = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j + i < len(nums):
                solutions.append(sum(nums[j:j + i+1]))
    maxNum=max(solutions)

    return maxNum

def maxSubArrayDP(nums=[5,-1,4]):
    j=0
    if len(nums)==0:
        return 0
    solution=[0]*len(nums)
    while j<len(solution):
        solution[j]=max(solution[j-1]+nums[j],nums[j])
        j+=1
    return max(solution)


print(maxSubArray())
print(maxSubArrayDP())
