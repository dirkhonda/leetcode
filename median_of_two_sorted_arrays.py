def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    length = len(nums1)
    mid = length // 2
    
    if not nums1:
        return None
    if len(nums1) == 1:
        return nums1[0]
    
    if length % 2 == 0:
        return (nums1[mid-1] + nums1[mid]) / 2
    else:
        return nums1[mid]


nums1 = [1, 3]
nums2 = [2]
# not optimal
print(findMedianSortedArrays(nums1, nums2))
