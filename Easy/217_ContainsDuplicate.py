def containsDuplicate( nums=[1,2,3,4,5]):
    if len(set(nums)) < len(nums):
        return True
    else:
        return False
print(containsDuplicate())