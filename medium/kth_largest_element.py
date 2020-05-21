# 215. Kth Largest Element in an Array - MEDIUM

# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.



def findKthLargest(nums, k) -> int: 
    k = len(nums) - k
    def swap(i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]
    def qsSort(i, j, arr):
        pivot = arr[j]
        wall = i
        while i < j:
            if arr[i] < pivot:
                swap(i, wall, arr)
                wall += 1
            i += 1
        swap(wall, j, arr)
        return wall
    i, j = 0, len(nums) - 1
    while i <= j:
        pivot = qsSort(i, j, nums)
        if pivot == k:
            return nums[k]
        if pivot > k:
            j = pivot - 1
        elif pivot < k:
            i = pivot + 1
    return nums[k]

print(findKthLargest([3,2,1,5,6,4], 2), 5)
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)
