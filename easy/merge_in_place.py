# 88. Merge Sorted Array - EASY

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]


def merge(nums1, m, nums2, n):
    m, n = m-1, n-1
    for idx in range(len(nums1) - 1, -1, -1):
        if n >= 0 and m >= 0 and nums2[n] > nums1[m]:
            nums1[idx] = nums2[n]
            n -= 1
        elif n >= 0 and m >= 0 and nums1[m] >= nums2[n]:
            nums1[idx] = nums1[m]
            m -= 1
        elif n < 0:
            nums1[idx] = nums1[m]
            m -= 1
        elif m < 0:
            nums1[idx] = nums2[n]
            n -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
