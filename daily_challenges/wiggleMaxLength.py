class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        ans = [1] * len(nums)
        diff = [nums[i]-nums[i-1] for i in range(1,len(nums))]
        for r in range(1,len(diff)):
            for l in range(r-1, -1, -1):
                if diff[r] < 0 and diff[l] > 0: ans[r] = ans[l] + 1; break
                if diff[r] > 0 and diff[l] < 0: ans[r] = ans[l] + 1; break
        return max(ans) + 1 if max(nums) != min(nums) else 1
