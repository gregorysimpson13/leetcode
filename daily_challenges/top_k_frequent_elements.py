# Top K Frequent Elements
# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:

# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# You can return the answer in any order.
from collections import Counter
from typing import List
import heapq
class Solution:
    @staticmethod
    def find_pivot(left, right, arr):
        pivot_value = arr[right][0]
        wall = left
        while left < right:
            if arr[left][0] > pivot_value:
                arr[left], arr[wall] = arr[wall], arr[left]
                wall = wall + 1
            left = left + 1
        arr[right], arr[wall] = arr[wall], arr[right]   
        return right
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k: return nums
        frequency_dict = Counter(nums)
        frequency_list = [(freq, val) for val, freq in frequency_dict.items()]
        left, right = 0, len(frequency_list) - 1
        while left <= right:
            pivot = self.find_pivot(left, right, frequency_list)
            if pivot == k - 1:
                break
            if pivot < k - 1:
                left = pivot + 1
            if pivot > k - 1:
                right = pivot - 1
        return [val[1] for val in frequency_list[:k]]
print(Solution().topKFrequent([1,1,1,2,2,3], 2))
print(Solution().topKFrequent([1,2], 2))
print(Solution().topKFrequent([3,0,1,0], 1))