# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

# Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

# Example 1:

# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
# Example 2:

# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4 
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
# Example 3:

# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3


import heapq
from collections import defaultdict
def longestSubarray(nums, limit) -> int:
    max_length = 1
    min_heap, max_heap = [nums[0]], [-1 * nums[0]]
    min_removed_dict = defaultdict(int)
    max_removed_dict = defaultdict(int)
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    start, end = 0, 0
    while end < len(nums) - 1:
        while abs(min_heap[0] - (-1 * max_heap[0])) <= limit:
            max_length = max(max_length, (end - start) + 1)
            if end >= len(nums) - 1: break
            end = end + 1
            heapq.heappush(min_heap, nums[end])
            heapq.heappush(max_heap, -1 * nums[end])
        left_item = nums[start]
        start = start + 1
        min_removed_dict[left_item] += 1
        max_removed_dict[left_item] += 1
        while min_removed_dict[min_heap[0]] > 0:
            min_removed_dict[min_heap[0]] -= 1
            heapq.heappop(min_heap)
        while max_removed_dict[-1 * max_heap[0]] > 0:
            max_removed_dict[-1 * max_heap[0]] -= 1
            heapq.heappop(max_heap)
    return max_length



print(longestSubarray([8,2,4,7], 4), 2)
print(longestSubarray([10,1,2,4,7,2], 5), 4)
print(longestSubarray([4,2,2,2,4,4,2,2], 0), 3)