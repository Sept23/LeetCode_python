def checkPossibility(nums=[4,2,5,4]):
    '''
    Because of the condition nums[i] <= nums[i+1], we iterate through array and have knowledge of two parts:
    1.following Increasing order(Non decreasing) element (start from the left)
    2. unknown ordering (start at the current i)

    On the left checked part, we have 0th, 1th ... i-1th elements are increasing order(Non decreasing), in order to be an increasing order, the next i element must be larger thani-1th element.
    Two cases:

    nums[i-1] > nums[i+1], [3,4,2,3] for example. if we are at 1th position, 0th's 3 > 2th's 2, since 3 is in the ordered part, the number after 3 must be larger than or equal to 3. Thus, we need to modify 2th's 2, which is nums[i+1] = nums[i].
    nums[i-1] < nums[i+1], [1,4,2,3] for example. 1 is in the order, the number after 1 must be larger than or equal to 1. In this case, we modify ith element, which is nums[i] = nums[i+1].
    :param nums:
    :return:
    '''
    # O(n) time, O(1) space, iterate each element one by one
    check = False
    for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            continue
        else:
            # modify one time, make the modification as smaller as possible
            # case: first element
            if i == 0:
                nums[i] = nums[i + 1]
                check = True
            else:
                # nums[i-1] <= nums[i] since we pass condition from last check of nums[i] <= nums[i+1]
                if not check:
                    if nums[i - 1] > nums[i + 1]:
                        nums[i + 1] = nums[i]
                    else:
                        nums[i] = nums[i + 1]
                    check = True
                else:
                    return False
    return True
print(checkPossibility())