# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:

# Input:nums = [1,1,1], k = 2
# Output: 2
 

# Constraints:

# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

def subarraySumNaive(nums, k: int) -> int:
    result = 0
    for i in range(len(nums)):
        local_sum = 0
        for j in range(i, len(nums)):
            local_sum = local_sum + nums[j]
            if local_sum == k:
                result = result + 1
                break
    return result

def subarraySum(nums, k) -> int:
    result = 0
    numbers_dict = {}
    for i, val in enumerate(nums):
        numbers_dict[i] = val if i == 0 else numbers_dict[i-1] + val
        if numbers_dict[i] == k or numbers_dict[i] - val == k:
            result = result + 1
    print(numbers_dict)            
    return result

print(subarraySumNaive([1,1,1], 2), 2)
print(subarraySum([1,1,1], 2), 2)
print(subarraySum([1,1,1,-1], 2), 3)
print(subarraySum([1,1,1,-1,0,3,2], 4), 1)

# sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.