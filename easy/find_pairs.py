class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        seen, result = set(), set()
        for num in nums:
            if (num - k) in seen: result.add((num, num - k))
            seen.add(num)
        return len(result)