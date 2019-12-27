def containsNearbyDuplicate(nums=[1,2,3,1,2,3], k=2):
    record = {}
    Flag = False
    for ki, i in enumerate(nums):
        if i not in record:
            record[i] = [ki]
        else:
            if ki - record[i][-1] <=k:
                Flag = True
            # else:
            #     Flag = True
            record[i].append(ki)
    flag_len=False
    # print(record)
    for i in record:
        # print(len(record[i]))
        if len(record[i])>=2:
            flag_len=True
    # print(Flag)
    if flag_len:
        return Flag
    else:
        return False

def containsNearbyDuplicate( nums=[1,2,3,4,12,3], k=2):
        d = {}
        for i, v in enumerate(nums):
            if v in d.keys() and i - d[nums[i]] <= k:
                return True
            d[nums[i]] = i
        return False

print(containsNearbyDuplicate())