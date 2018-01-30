# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
#   nums1 = [1, 3], nums2 = [2]
#   The median is 2.0
#
# Example 2:
#   nums1 = [1, 2], nums2 = [3, 4]


# simple case
# edge case
# null case

def b_search(array, num, lo, hi):

    if lo == hi:
        return lo
    mid = (lo + hi) // 2
    if array[mid] == num:
        return mid
    if array[mid] > num:
        return b_search(array, num, lo, mid-1)
    if array[mid] < num:
        return b_search(array, num, mid+1, hi)
    

def find_median(nums1, nums2):
    for n in nums2:
        index = b_search(nums1, n, 0, len(nums1))
        nums1.insert(abs(index) + 1, n)
    a_len = len(nums1)

    if a_len % 2 == 0:
        return (nums1[a_len//2] + nums1[a_len//2+1]) // 2
    else:
         return nums1[a_len//2]

nums = []
for i in range(1, 10):
    nums.append(i)
nums.remove(6)

#print(b_search(nums, 6, 0, len(nums)))
print(find_median([1, 3], [2, 4, 5, 1]))

#print(b_search(nums, 1, 0, len(nums)))
#print(b_search(nums, 8, 0, len(nums)))
#print(nums[7])
