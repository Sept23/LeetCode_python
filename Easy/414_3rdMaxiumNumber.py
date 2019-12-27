def thirdMax(nums=[3,2,1]):
    # seen=[]
    # for i in nums:
    #     if i not in seen:
    #         seen.append(i)
    #     else:
    #         continue
    seen = list(set(nums))
    seen.sort(reverse=True)
    if len(seen) >= 3:
        return seen[2]
    else:
        return seen[0]
print(thirdMax())