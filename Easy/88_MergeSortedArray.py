def merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    L=nums1[:m]+nums2
    L.sort()
    for i in range(m+n):
        nums1[i]=L[i]

    # for i in range(m, m + n):
    #     nums1[i] = nums2[i - m]
    # nums1 = nums1[:m + n]
    # nums1.sort()
if __name__=="__main__":
    merge()