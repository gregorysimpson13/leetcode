class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not k or not nums: return
        k = k % len(nums)
        nums = nums[-k:] + nums[:-k]


# Runtime: O(n^2); beats 20.29%
# Space: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not k or not nums: return
        k = k % len(nums)
        for _ in range(-1, -k-1, -1):
            nums.insert(0, nums[-1])
            nums.pop()