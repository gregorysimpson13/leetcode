# 55. Jump Game - MEDIUM
# https://leetcode.com/problems/jump-game/

# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 3 * 10^4
# 0 <= nums[i][j] <= 10^5


def canJump(nums) -> bool:
    cache = {len(nums)-1: True}
    def jump(index):
        if index in cache:
            return cache[index]
        if nums[index] == 0:
            return False
        steps = nums[index]
        result = False
        for i in range(index, index + steps):
            result = result or jump(i+1)
        cache[index] = result
        return result
    return jump(0)

def canJumpGD(nums) -> bool:
    cache = {len(nums)-1: True}
    def jump(index):
        if index >= len(nums):
            return True
        if index in cache:
            return cache[index]
        if nums[index] == 0:
            return False
        steps = nums[index]
        result = False
        for i in range(index + steps, index, -1):
            result = jump(i)
            if result:
                break
        cache[index] = result
        return result
    return jump(0)

def canJumpGreedy(nums) -> bool:
    left, right = 0, nums[0]
    while left <= right:
        right = max(right, left + nums[left])
        left += 1
        if right >= len(nums):
            return True
    return False if left < len(nums) else True

print(canJumpGreedy([2,3,1,1,4]), True)
print(canJumpGreedy([3,2,1,0,4]), False)
print(canJumpGreedy([2,0]), True)
print(canJumpGreedy([0]), True)
