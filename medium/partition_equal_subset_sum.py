# 416. Partition Equal Subset sum
# https://leetcode.com/problems/partition-equal-subset-sum/

# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Note:

# Each of the array element will not exceed 100.
# The array size will not exceed 200.
 

# Example 1:

# Input: [1, 5, 11, 5]

# Output: true

# Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

# Example 2:

# Input: [1, 2, 3, 5]

# Output: false

# Explanation: The array cannot be partitioned into equal sum subsets.

'''
if one sum == sum/2 then we have reached the True condition
two decisions can be made - add item or do not add item to another array
2d array: sums and idx of nums
columns -> sums
rows -> index into nums
f(s-nums[i], i-1)
f(s, i-1)
'''



def canPartition(nums) -> bool:
    partition_sum = sum(nums)
    if partition_sum % 2 != 0:
        return False
    dp = [[0]*((partition_sum//2)+1) for i in range(len(nums))]
    for nums_i in range(len(dp)):
        for sum_value in range(len(dp[0])):
            if sum_value == 0:
                dp[nums_i][sum_value] = True
            elif nums_i == 0:
                dp[nums_i][sum_value] = False
            else:
                val = dp[nums_i-1][sum_value]
                idx = sum_value-nums[nums_i]
                if idx >= 0:
                    val |= dp[nums_i-1][sum_value-nums[nums_i]]
                dp[nums_i][sum_value] = val
    return dp[len(dp)-1][len(dp[0])-1]
    


print(canPartition([1,5,11,5]),True)
print(canPartition([1,2,3,5]),False)
print(canPartition([4,1,2,3,16]),False)
print(canPartition([1,2,3,5,4,13]),True)
print(canPartition([4,2]),False)
print(canPartition([4]),False)