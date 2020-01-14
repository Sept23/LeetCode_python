import collections
def findShortestSubArray(nums=[1,1,1]):
    dict_list=collections.Counter(nums)
    maxFreq=max(dict_list.values())
    candidate=[]
    for i in dict_list.keys():
        if dict_list.get(i)==maxFreq:
            candidate.append(i)
    length=[]
    for val in candidate:
        first=nums.index(val)
        reversedList=list(reversed(nums))
        last=reversedList.index(val)
        last=len(nums)-last-1
        # print(first,last)
        lengthVal=last-first+1
        length.append(lengthVal)
    return min(length)

def findShortestSubArray2(nums=[1,2,2,3,1]):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        print(left)
        print(right)
        print(count)
        return ans
print(findShortestSubArray2())
