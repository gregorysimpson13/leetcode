# 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/

# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

# Example 1:
# Input: [3, 2, 1]

# Output: 1

# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]

# Output: 2

# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]

# Output: 1

# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.

def thirdMax(nums: List[int]) -> int:
    nums = list(set(nums))
    if len(nums) < 3:
        return max(nums)
    l, r = 0, len(nums) - 1
    def swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]
    def pivot(i, j):
        p = nums[j]
        left, right = i, j - 1
        wall = left
        while left <= right:
            if nums[left] < p:
                swap(left, wall)
                wall = wall + 1
            left = left + 1
        swap(j, wall)
        return wall
    while l <= r:
        p = pivot(l, r)
        if p == len(nums) - 3:
            return nums[p]
        if p < len(nums) - 3:
            l = p + 1
        if p > len(nums) - 3:
            r = p - 1
    return nums[-3]