class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        curr, count = 0, 0
        while left < right and left < len(nums):
            if nums[left] == curr: count += 1
            else: count = 1; curr = nums[left]
            if count > 2:
                for i in range(left+1, right):
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                right -= 1
            else: left += 1
        return right