# 645. Set Mismatch - EASY
# https://leetcode.com/problems/set-mismatch/

# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Note:
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.


def findErrorNums(nums):
    duplicate = None
    max_num = float('-inf')
    nums_set = set()
    for num in nums:
        max_num = max(num, max_num)
        if num in nums_set:
            duplicate = num
        nums_set.add(num)
    for i in range(1, max_num):
        if i not in nums_set:
            return [duplicate, i]
    return [duplicate, max_num+1]
    
    


findErrorNums([2,3,4,5])
print(findErrorNums([1,2,2,4]))
print(findErrorNums([2,2]))
print(findErrorNums([1,1]))
print(findErrorNums([3,2,3,4,6,5]))