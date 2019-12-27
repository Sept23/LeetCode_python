def rotate(nums=[1,2,3,4,5,6,7],k=3):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    nums[:] = nums[n - k % n:] + nums[:n - k % n]

    # n = len(nums)
    # nums[:] = nums[n - k % n:] + nums[:n - k % n]

    print(nums)
    # for i in range(k):
    #     nums.insert(0,nums[-1])
    #     nums.pop()
    #     print(nums)
    # print(nums)
def rotateQuick(nums=[1,2,3,4,5,6,7],k=3):
    """
    Do not return anything, modify nums in-place instead.
    """
    # L = nums[-k:] + nums[:k + 1]
    # nums = L[:]
    # print(nums.pop())
    for i in range(k):
        nums.insert(0,nums[-1])
        nums.pop()
        print(nums)
rotate()