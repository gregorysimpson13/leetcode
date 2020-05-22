# 169. Majority Element - EASY
# https://leetcode.com/problems/majority-element/

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2
from collections import defaultdict

def majorityElement(nums) -> int:
    cache = defaultdict(int)
    for n in nums:
        cache[n] += 1
        if cache[n] > len(nums) // 2:
            return n
    return None