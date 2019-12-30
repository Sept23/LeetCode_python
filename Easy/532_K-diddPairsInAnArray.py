import collections


def findPairs(nums=[3,1,4,1,5], k=2):
    pair=0
    if k<0:
        return pair
    elif k>0:
        nums=set(nums)
        nums_=list(nums)
        for idx, v in enumerate(nums_):
            potentialnums1=v-k
            potentialnums2=v+k
            # print(potentialnums1,potentialnums2)

            if potentialnums1 in nums:
                pair+=1
            if potentialnums2 in nums:
                pair+=1
            nums.remove(v)
    else:
        numbers = collections.defaultdict(int)
        for number in nums:
            numbers[number] += 1

        for occurences in numbers.values():
            if (occurences >= 2):
                pair += 1
    return pair

def findPairsCounter(nums=[3,1,4,1,5], k=2):
        if k < 0:
            return 0

        import collections
        n_frq_dict = collections.Counter(nums)
        ans = 0
        for n, frq in n_frq_dict.items():
            m = n + k
            if n == m:
                if n_frq_dict[m] > 1:
                    ans += 1
            else:
                if m in n_frq_dict:
                    ans += 1

        return ans
print(findPairsCounter())