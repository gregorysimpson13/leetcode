# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

# [10, 5, 2, 6], k = 100
# 10, 5, 10-5, 2, 5-2, 6, 5-2-6, 2-6


# [1, 2, 3, 4], k = 1000
# 1, 2, 1-2, 3, 1-2-3, 2-3, 4, 3-4, 2-3-4, 1-2-3-4


# [20, 0, 1, 5, 10], k = 50
# 20, 20-0, 1
# Runtime: O(n); beats 99.44%
# Space: O(1)
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = right = res = 0
        product = 1
        for right in range(len(nums)):
            product = product * nums[right]
            while product >= k and left < right:
                product = product / nums[left]
                left += 1            
            if product < k: res += (right-left) + 1
        return res