# 674. Longest Continuous Increasing Subsequence
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1. 


def findLengthOfLCIS(nums) -> int:
    max_continuous = 0 if nums == [] else 1
    local = 1
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            local = local + 1
        else:
            local = 1
        max_continuous = max(max_continuous, local)
    return max_continuous
    


print(findLengthOfLCIS([1,3,5,4,7]), 3)
print(findLengthOfLCIS([9,1,3,5,4,7]), 3)
print(findLengthOfLCIS([2,2,2,2,2]), 1)
print(findLengthOfLCIS([2]), 1)
print(findLengthOfLCIS([]), 0)