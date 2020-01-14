def findMaxAverage(nums=[0,4,0,3,2], k=1):
    length = len(nums)
    sum_=[]
    sum_.append(sum(nums[0:k]))
    print(sum_)
    for i in range(1, length):
        if i + k <= length:
            sum_.append(sum_[i-1] - nums[i - 1] + nums[i + k - 1])
        else:
            break
    return max(sum_)/k
print(findMaxAverage())