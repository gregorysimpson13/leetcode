# 35 - Search Insert Position - EASY

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2
# Example 2:

# Input: [1,3,5,6], 2
# Output: 1
# Example 3:

# Input: [1,3,5,6], 7
# Output: 4
# Example 4:

# Input: [1,3,5,6], 0
# Output: 0

def searchInsert(nums, target) -> int:
    if target < nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)
    for i in range(len(nums)):
        if target == nums[i]:
            return i
        if i-1 >= 0 and nums[i-1] < target and nums[i] > target:
            return i
    return 0


print(searchInsert([1,3,5,6], 0), 0)
print(searchInsert([1,3,5,6], 2), 1)
print(searchInsert([1,3,5,6], 7), 4)


def searchInsertQuick(nums, target) -> int:
    if target < nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)
    def search(left, right):
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if mid + 1 < len(nums) and nums[mid] < target and target < nums[mid+1]:
            return mid + 1
        if nums[mid] > target: return search(left, mid-1)
        if nums[mid] < target: return search(mid+1, right)
    return search(0, len(nums) - 1)


print("Binary Search for Target")
print(searchInsertQuick([1,3,5,6], 0), 0)
print(searchInsertQuick([1,3,5,6], 2), 1)
print(searchInsertQuick([1,3,5,6], 7), 4)
print(searchInsertQuick([1,3], 2), 1)
print(searchInsertQuick([1,3], 3), 1)